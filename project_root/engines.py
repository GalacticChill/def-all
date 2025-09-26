from rapsheet import RapsheetEntry

class Engine:
    def __init__(self, id: int, pieces: list):
        self.id = id
        self.pieces = pieces
        self.rapsheet = []

    def run_cycle(self, stock) -> None:
        """Simulate buying & selling for all pieces in this engine."""
        for piece in self.pieces:
            # Period a → assign stock
            piece.stock_identity = stock.symbol
            piece.period = "b"

            # Period b → simulate return
            change = stock.simulate_return()
            piece.value *= (1 + change)

            # Record in rapsheet
            self.rapsheet.append(RapsheetEntry(stock.symbol, change))

            # Reset to period a
            piece.period = "a"
