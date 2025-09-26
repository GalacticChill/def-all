# stocks.py
import random

class Stock:
    """
    Represents a single stock with a symbol and a price history.
    Price evolves each cycle (default: random walk).
    """

    def __init__(self, symbol: str, start_price: float = 100.0):
        self.symbol = symbol
        self.price_history = [start_price]

    @property
    def current_price(self) -> float:
        return self.price_history[-1]

    def next_price(self):
        """
        Advance to the next price.
        Default: random walk with ~1% standard deviation.
        """
        last_price = self.current_price
        change_factor = 1 + random.gauss(0, 0.01)  # mean 0%, stdev 1%
        new_price = max(0.01, last_price * change_factor)  # no zero/negative
        self.price_history.append(new_price)
        return new_price

    def __repr__(self):
        return f"<Stock {self.symbol} price={self.current_price:.2f}>"


class Market:
    """
    Holds a collection of stocks and updates them each cycle.
    """

    def __init__(self, stock_symbols: list[str]):
        self.stocks: dict[str, Stock] = {
            sym: Stock(sym) for sym in stock_symbols
        }

    def update(self):
        """
        Advance all stocks to their next price.
        """
        for stock in self.stocks.values():
            stock.next_price()

    def get_price(self, symbol: str) -> float:
        return self.stocks[symbol].current_price

    def __repr__(self):
        stock_list = ", ".join(
            f"{sym}: {s.current_price:.2f}" for sym, s in self.stocks.items()
        )
        return f"<Market {stock_list}>"
