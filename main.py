from agents.beacon_agent import BeaconAgent

peer_map = {
    "N-03": ("127.0.0.1", 9011),
    "N-07": ("127.0.0.1", 9012)
}

agent = BeaconAgent("N-01", peer_map)
agent.loop(interval=15)
