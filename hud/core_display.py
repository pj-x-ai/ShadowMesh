# core_display.py – CrossComAI HUD Node Visualizer

import json
import tkinter as tk
from termcolor import colored
from datetime import datetime

class NodeHUD:
    def __init__(self):
        self.nodes = {}

    def receive(self, enc_packet, cipher_engine):
        try:
            raw = cipher_engine.decrypt(enc_packet).decode()
            data = eval(raw)  # assume signed JSON dict
            node_id = data['node_id']
            self.nodes[node_id] = {
                "status": "online",
                "arch": data['arch'],
                "os": data['system'],
                "last": datetime.utcnow()
            }
            self.display_cli(node_id)
        except Exception as e:
            print(colored(f"[✖] Decryption or Signal Parsing Failed: {e}", "red"))

    def display_cli(self, node_id):
        node = self.nodes[node_id]
        stamp = node['last'].strftime("%H:%M:%S")
        msg = f"[{stamp}] {node_id} · {node['os']}/{node['arch']} · {colored('ONLINE', 'green')}"
        print(msg)

    def launch_gui(self):
        root = tk.Tk()
        root.title("CrossComAI - Node HUD")
        canvas = tk.Canvas(root, width=400, height=400, bg='black')
        canvas.pack()

        def update_hud():
            canvas.delete("all")
            now = datetime.utcnow()
            y = 30
            for nid, info in self.nodes.items():
                delta = (now - info["last"]).total_seconds()
                color = "green" if delta < 30 else "yellow" if delta < 60 else "red"
                status = "ONLINE" if delta < 30 else "LAGGED" if delta < 60 else "OFFLINE"
                canvas.create_text(200, y, text=f"{nid} [{status}]", fill=color, font=("Consolas", 12))
                y += 30
            root.after(1000, update_hud)

        update_hud()
        root.mainloop()
