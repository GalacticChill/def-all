from pieces import Piece
from engines import Engine
from stocks import Market
from simulator import Simulator
from council import Council
from visualization import Visualization

if __name__ == "__main__":
    # Setup market
    market = Market(["AAPL", "TSLA", "MSFT", "GOOG"])

    # Create pieces for two engines
    pieces_engine1 = [Piece(id=i, value=100.0) for i in range(3)]
    pieces_engine2 = [Piece(id=i+100, value=200.0) for i in range(2)]

    # Two engines with different starting capital
    engine1 = Engine("Engine_1", pieces_engine1, market)
    engine2 = Engine("Engine_2", pieces_engine2, market)

    council = Council()
    viz = Visualization()

    # Simulator handles both engines
    sim = Simulator([engine1, engine2], council, market)

    # Run for 30 cycles
    for _ in range(30):
        sim.run_cycle()
        # Record data for each engine
        viz.record_stock_prices(market)
        viz.record_engine_value(engine1)
        viz.record_engine_value(engine2)
        viz.record_allbank(council)

    # Show plots
    viz.plot()
