class RapsheetEntry:
    def __init__(self, stock: str, percent_gain: float):
        self.stock = stock
        self.percent_gain = percent_gain

    def __repr__(self):
        return f"{self.stock}: {self.percent_gain:+.2%}"
