class Council:
    def __init__(self):
        pass

    def review_engine(self, engine):
        """Naive council: print last trade results only."""
        if engine.rapsheet:
            last_entry = engine.rapsheet[-1]
            print(f"Council reviewing Engine {engine.id}: {last_entry}")
