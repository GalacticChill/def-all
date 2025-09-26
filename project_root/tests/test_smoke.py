from pieces import Piece
from stocks import Stock
from engines import Engine

def test_piece_lifecycle():
    p = Piece(1)
    assert p.period == "a"

    s = Stock("ABC")
    e = Engine(1, [p])
    e.run_cycle(s)

    assert p.period == "a"  # should return to cash
    assert len(e.rapsheet) == 1
