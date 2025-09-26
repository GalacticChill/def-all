# simulator.py
from engines import Engine
from council import Council
from pieces import Piece

class Simulator:
    """
    The Simulator runs cycles across all engines, coordinating:
    - Period a: pieces are cash, council may adjust value/stock
    - Period b: pieces are stock, engines process them
    """

    def __init__(self, engines: list[Engine], council: Council):
        self.engines = engines
        self.council = council
        self.cycle_count = 0

    def run_cycle(self):
        """
        Runs a full a→b cycle for all engines.
        """
        self.cycle_count += 1
        print(f"\n--- Cycle {self.cycle_count} ---")

        # === Period a (cash state) ===
        print("Period a: Council adjusts pieces...")
        for engine in self.engines:
            self.council.review_engine(engine)

        # === Period b (stock state) ===
        print("Period b: Engines process trades...")
        for engine in self.engines:
            engine.process_pieces()

        print("--- End of cycle ---")

    def status_report(self):
        """
        Prints out the current state of all engines and their pieces.
        """
        print(f"\n===== Simulator Status after {self.cycle_count} cycles =====")
        for i, engine in enumerate(self.engines, start=1):
            print(f"\nEngine {i}: {engine.name}")
            print("Pieces:")
            for piece in engine.pieces:
                print(f"  {piece}")
            print("Rapsheet:")
            for entry in engine.rapsheet:
                print(f"  {entry}")
        print("============================================================")
