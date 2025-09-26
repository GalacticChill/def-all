# engines.py

from pieces import Piece
from stocks import Market
import random


class Engine:
    """
    An Engine invests pieces in stocks through two periods:
    - Period a: pieces are cash, stock identity may change
    - Period b: pieces are stock, engine simulates a buy/sell
    Rapsheet logs all trades as percent gain/loss.
    """

    def __init__(self, name: str, pieces: list[Piece], market: Market):
        self.name = name
        self.pieces = pieces
        self.market = market
        self.rapsheet: list[dict] = []

    def process_pieces(self):
        """
        Move each piece through its cycle:
        - If in period a: assign a stock identity (choose randomly for now).
        - If in period b: sell at current market price, record gain/loss.
        """
        for piece in self.pieces:
            if piece.is_in_period_a:
                # Assign stock identity randomly
                stock_symbol = random.choice(list(self.market.stocks.keys()))
                piece.stock_identity = stock_symbol
                # Mark piece as "invested" (period b)
                piece.is_in_period_a = False
                piece.buy_price = self.market.get_price(stock_symbol)

            else:
                # Selling phase (period b)
                stock_symbol = piece.stock_identity
                sell_price = self.market.get_price(stock_symbol)
                buy_price = getattr(piece, "buy_price", sell_price)

                percent_change = (sell_price - buy_price) / buy_price

                # Update piece value
                piece.value *= (1 + percent_change)

                # Log result in rapsheet
                self.rapsheet.append({
                    "stock": stock_symbol,
                    "gain": percent_change,
                    "piece_id": piece.id
                })

                # Reset piece to cash (period a)
                piece.stock_identity = None
                piece.is_in_period_a = True
                delattr(piece, "buy_price")  # clean up temporary field

    def __repr__(self):
        return f"<Engine {self.name} pieces={len(self.pieces)}>"
