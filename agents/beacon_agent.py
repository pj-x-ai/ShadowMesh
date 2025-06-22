# beacon_agent.py – Self-Reporting Node Agent (AES/XOR Encrypted)

import time
import platform
from crypto.cipher_engine import CipherEngine
from ops.router import SignalRouter

class BeaconAgent:
    def __init__(self, node_id, peers, seed="mesh-shard-777"):
        self.node_id = node_id
        self.router = SignalRouter(peers)
        self.cipher = CipherEngine(seed)

    def pulse(self):
        signature = {
            "node_id": self.node_id,
            "system": platform.system(),
            "arch": platform.machine(),
            "heartbeat": time.time()
        }
        enc_payload = self.cipher.encrypt(str(signature).encode())
        self.router.broadcast({"type": "beacon", "payload": enc_payload})

    def loop(self, interval=20):
        while True:
            self.pulse()
            print(f"[{self.node_id}] Beacon sent.")
            time.sleep(interval)
