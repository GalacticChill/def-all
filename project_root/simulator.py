from engines import Engine
from pieces import Piece
from stocks import Stock
from council import Council

class Simulator:
    def __init__(self, num_pieces=10, num_engines=2, num_stocks=3):
        self.pieces = [Piece(id=i) for i in range(num_pieces)]
        self.engines = []
        self.stocks = [Stock(f"STK{i}") for i in range(num_stocks)]
        self.council = Council()

        # Evenly divide pieces among engines
        per_engine = num_pieces // num_engines
        for e in range(num_engines):
            engine_pieces = self.pieces[e*per_engine:(e+1)*per_engine]
            self.engines.append(Engine(e, engine_pieces))

    def run(self, cycles=5):
        for c in range(cycles):
            print(f"\n--- Cycle {c+1} ---")
            for engine in self.engines:
                stock = self.stocks[c % len(self.stocks)]
                engine.run_cycle(stock)
                self.council.review_engine(engine)
