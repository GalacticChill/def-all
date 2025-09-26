# council.py

from engines import Engine
from pieces import Piece
from allbank import AllBank


class Council:
    """
    Council reviews engines and makes redistribution decisions:
      - Rewards engines/pieces that gained value
      - Penalizes underperformers
      - Uses AllBank if transfers must be delayed
    """

    def __init__(self):
        self.allbank = AllBank()

    def review_engine(self, engine: Engine):
        """
        Inspect the engine's most recent trades and adjust pieces accordingly.
        Simple rule:
          - If last trade gained > 0, reward piece with bonus.
          - If last trade lost < 0, penalize piece by moving value to AllBank.
        """
        if not engine.rapsheet:
            return  # no trades yet

        last_trade = engine.rapsheet[-1]
        piece_id = last_trade["piece_id"]
        gain = last_trade["gain"]

        # Find the piece that was traded
        piece = next((p for p in engine.pieces if p.id == piece_id), None)
        if piece is None:
            return

        if piece.is_in_period_a:  # only touch during cash phase
            if gain > 0:
                # Reward with 5% bonus from AllBank (if available)
                bonus = self.allbank.withdraw(min(self.allbank.balance, piece.value * 0.05)) if self.allbank.balance > 0 else 0
                piece.value += bonus
                print(f"[Council] Rewarded Piece {piece.id} with {bonus:.2f} (gain {gain:.2%})")
            elif gain < 0:
                # Penalize: remove 5% of value and send to AllBank
                penalty = piece.value * 0.05
                piece.value -= penalty
                self.allbank.deposit(penalty)
                print(f"[Council] Penalized Piece {piece.id} by {penalty:.2f} (loss {gain:.2%})")
        else:
            # If piece is in period b, skip for now
            pass

    def status(self):
        return f"Council AllBank balance={self.allbank.balance:.2f}"
