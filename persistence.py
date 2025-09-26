# persistence.py
import json
import pickle

def save_state(filename, simulator):
    """Save the simulator state to a file using pickle."""
    with open(filename, "wb") as f:
        pickle.dump(simulator, f)
    print(f"[Persistence] Simulator state saved to {filename}")

def load_state(filename):
    """Load simulator state from file."""
    with open(filename, "rb") as f:
        simulator = pickle.load(f)
    print(f"[Persistence] Simulator state loaded from {filename}")
    return simulator

def load_config(filename="config.json"):
    """Load configuration from JSON file."""
    with open(filename, "r") as f:
        config = json.load(f)
    return config
