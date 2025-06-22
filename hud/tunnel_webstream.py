# webstream.py – WebSocket HUD Streamer with Encrypted Tunneling

import asyncio
import websockets
import json
from crypto.cipher_engine import CipherEngine

class HUDWebStreamer:
    def __init__(self, node_hud, key_seed="tunnel-salt"):
        self.node_hud = node_hud
        self.engine = CipherEngine(key_seed)

    async def stream_nodes(self, websocket, path):
        while True:
            try:
                feed = {
                    node_id: {
                        "status": node["status"],
                        "arch": node["arch"],
                        "os": node["os"],
                        "last": str(node["last"])
                    }
                    for node_id, node in self.node_hud.nodes.items()
                }
                encrypted = self.engine.encrypt(json.dumps(feed).encode())
                await websocket.send(encrypted)
                await asyncio.sleep(2)
            except Exception as e:
                print("[✖] Webstream transmission error:", str(e))
                break

    def run(self, host="localhost", port=8999):
        print(f"[🛰️] WebSocket HUD Tunnel running at ws://{host}:{port}/")
        start_server = websockets.serve(self.stream_nodes, host, port)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
