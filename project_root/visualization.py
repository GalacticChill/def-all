# visualization.py

import matplotlib.pyplot as plt

class Visualization:
    def __init__(self):
        self.stock_history = {}     # stock -> [prices]
        self.engine_history = {}    # engine_name -> [total_value]
        self.allbank_history = []   # [balance]

    def record_stock_prices(self, market):
        """Store the current prices of all stocks."""
        for stock, price in market.prices.items():
            if stock not in self.stock_history:
                self.stock_history[stock] = []
            self.stock_history[stock].append(price)

    def record_engine_value(self, engine):
        """Store total portfolio value of an engine."""
        total_value = sum(p.value for p in engine.pieces)
        if engine.name not in self.engine_history:
            self.engine_history[engine.name] = []
        self.engine_history[engine.name].append(total_value)

    def record_allbank(self, council):
        """Store current AllBank balance."""
        self.allbank_history.append(council.allbank.balance)

    def plot(self):
        fig, axs = plt.subplots(3, 1, figsize=(10, 12))

        # --- Stock Prices ---
        for stock, prices in self.stock_history.items():
            axs[0].plot(prices, label=stock)
        axs[0].set_title("Stock Prices")
        axs[0].set_ylabel("Price")
        axs[0].legend()

        # --- Engine Values ---
        for eng, values in self.engine_history.items():
            axs[1].plot(values, label=eng)
        axs[1].set_title("Engine Portfolio Values")
        axs[1].set_ylabel("Value")
        axs[1].legend()

        # --- AllBank Balance ---
        axs[2].plot(self.allbank_history, color="purple")
        axs[2].set_title("Council AllBank Balance")
        axs[2].set_ylabel("Balance")

        plt.tight_layout()
        plt.show()
