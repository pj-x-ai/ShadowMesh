# hud_launch.py — CrossComAI HUD Sync + WebStream Activation

from hud.core_display import NodeHUD
from hud.webstream import HUDWebStreamer

if __name__ == "__main__":
    print("[🧠] Initializing CrossComAI HUD Interface...")
    hud = NodeHUD()
    streamer = HUDWebStreamer(hud)
    streamer.run()
