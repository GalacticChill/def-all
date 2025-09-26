import random

class Stock:
    def __init__(self, symbol: str):
        self.symbol = symbol

    def simulate_return(self) -> float:
        """Return a random percent change (e.g., -0.05 = -5%)."""
        return random.uniform(-0.1, 0.1)
