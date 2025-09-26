class Council:
    def __init__(self, allbank):
        self.allbank = allbank
        self.decision_log = []

    def transfer_value(self, from_piece, to_piece, amount: float):
        if from_piece.period == "b" or to_piece.period == "b":
            raise ValueError("Cannot transfer value while a piece is in period b.")
        if amount > from_piece.value:
            raise ValueError("Insufficient funds in source piece.")
        from_piece.set_value(from_piece.value - amount)
        to_piece.set_value(to_piece.value + amount)
        self.decision_log.append(
            {"action": "transfer", "from": from_piece.id, "to": to_piece.id, "amount": amount}
        )

    def review_engine(self, engine):
        """For now: print last result."""
        if engine.rapsheet:
            last_entry = engine.rapsheet[-1]
            print(f"Council reviewing Engine {engine.id}: {last_entry}")
