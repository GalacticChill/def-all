class Piece:
    def __init__(self, id: int, value: float = 100.0, stock_identity: str = None):
        self.id = id
        self._value = value
        self.stock_identity = stock_identity
        self.period = "a"  # "a" = cash, "b" = stock

    @property
    def value(self):
        return self._value

    def set_value(self, new_value: float):
        if self.period == "b":
            raise ValueError("Cannot change value during period b (stock phase).")
        self._value = new_value

    def change_stock(self, new_stock: str):
        if self.period == "b":
            raise ValueError("Cannot change stock during period b (stock phase).")
        self.stock_identity = new_stock

    def __repr__(self):
        return f"<Piece {self.id}: {self._value:.2f}, stock={self.stock_identity}, period={self.period}>"
