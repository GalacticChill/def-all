# simulator.py

from engines import Engine
from council import Council
from stocks import Market


class Simulator:
    """
    The Simulator orchestrates the system:
      - Updates the market each cycle
      - Period a: council adjusts pieces (while they are cash)
      - Period b: engines trade pieces in stocks
      - Tracks cycles and reports system status
    """

    def __init__(self, engines: list[Engine], council: Council, market: Market):
        self.engines = engines
        self.council = council
        self.market = market
        self.cycle_count = 0

    def run_cycle(self):
        """
        Runs a full cycle (a → b).
        """
        self.cycle_count += 1
        print(f"\n=== Cycle {self.cycle_count} ===")

        # Step 1: Market moves
        print("Market updating prices...")
        self.market.update()

        # Step 2: Period a — Council adjustments
        print("Period a: Council reviews engines...")
        for engine in self.engines:
            self.council.review_engine(engine)

        # Step 3: Period b — Engines process trades
        print("Period b: Engines execute trades...")
        for engine in self.engines:
            engine.process_pieces()

        print(f"=== End of cycle {self.cycle_count} ===")

    def status_report(self):
        """
        Prints current state of engines, pieces, and market.
        """
        print(f"\n===== Status Report after {self.cycle_count} cycles =====")
        print("Market:", self.market)

        for i, engine in enumerate(self.engines, start=1):
            print(f"\nEngine {i}: {engine.name}")
            print("Pieces:")
            for piece in engine.pieces:
                print(f"  {piece}")
            print("Rapsheet:")
            for entry in engine.rapsheet[-5:]:  # show last 5 trades
                print(f"  {entry}")

        print("========================================================")
