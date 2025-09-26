class Piece:
    def __init__(self, id: int, value: float = 100.0, stock_identity: str = None):
        self.id = id
        self.value = value
        self.stock_identity = stock_identity
        self.period = "a"  # "a" = cash, "b" = stock

    def __repr__(self):
        return f"<Piece {self.id}: {self.value:.2f}, stock={self.stock_identity}, period={self.period}>"
