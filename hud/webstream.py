# webstream.py – Encrypted WebSocket HUD Streamer (CrossComAI-Compatible)

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
                # Gather live node intel
                feed = json.dumps(self.node_hud.nodes)
                
                # Encrypt the payload using AES/XOR hybrid cipher
                encrypted = self.engine.encrypt(feed.encode())

                # Transmit to connected WebSocket listener
                await websocket.send(encrypted)

                await asyncio.sleep(2)

            except Exception as e:
                print("[✖] HUD WebSocket Error:", str(e))
                break

    def run(self, host="localhost", port=8999):
        print(f"[🛰️] CrossComAI Encrypted Tunnel at ws://{host}:{port}/")
        start_server = websockets.serve(self.stream_nodes, host, port)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
