# council.py

from engines import Engine
from pieces import Piece
from allbank import AllBank

class Council:
    def __init__(self):
        self.allbank = AllBank()

    def review_engine(self, engine: Engine):
        """
        Inspect the engine's most recent trades and adjust pieces accordingly.
        """
        if not engine.rapsheet:
            return

        last_trade = engine.rapsheet[-1]
        piece_id = last_trade["piece_id"]
        gain = last_trade["gain"]

        piece = next((p for p in engine.pieces if p.id == piece_id), None)
        if piece is None:
            return

        if piece.is_in_period_a:
            if gain > 0:
                bonus = self.allbank.withdraw(min(self.allbank.balance, piece.value * 0.05)) if self.allbank.balance > 0 else 0
                piece.value += bonus
                print(f"[Council] Rewarded Piece {piece.id} with {bonus:.2f} (gain {gain:.2%})")
            elif gain < 0:
                penalty = piece.value * 0.05
                piece.value -= penalty
                self.allbank.deposit(penalty)
                print(f"[Council] Penalized Piece {piece.id} by {penalty:.2f} (loss {gain:.2%})")

    def review_all_engines(self, engines):
        """NEW: Review multiple engines per cycle."""
        for engine in engines:
            self.review_engine(engine)

    def status(self):
        return f"Council AllBank balance={self.allbank.balance:.2f}"
