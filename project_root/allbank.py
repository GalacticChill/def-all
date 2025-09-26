# allbank.py

from pieces import Piece

class AllBank:
    """
    The AllBank temporarily stores value as pure cash.
    Rules:
      - Value goes here if the Council hasn’t decided which piece it belongs to.
      - Value also goes here if a target piece is stuck in period b (stock mode).
    Goal: keep AllBank as empty as possible.
    """

    def __init__(self):
        self._balance: float = 0.0

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self._balance += amount
        print(f"[AllBank] Deposited {amount:.2f}, new balance: {self._balance:.2f}")

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")
        if amount > self._balance:
            raise ValueError("Not enough funds in AllBank.")
        self._balance -= amount
        print(f"[AllBank] Withdrew {amount:.2f}, new balance: {self._balance:.2f}")
        return amount

    def empty_into_piece(self, piece: Piece):
        """
        Transfer all available cash into a piece (if piece is in period a).
        """
        if not piece.is_in_period_a:
            print(f"[AllBank] Piece {piece.id} in period b, cannot transfer now.")
            return
        if self._balance > 0:
            piece.value += self._balance
            print(f"[AllBank] Moved {self._balance:.2f} into Piece {piece.id}.")
            self._balance = 0.0

    @property
    def balance(self) -> float:
        return self._balance

    def __repr__(self):
        return f"<AllBank balance={self._balance:.2f}>"
