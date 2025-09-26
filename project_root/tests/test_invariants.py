import pytest
from simulator import Simulator, total_value

def test_value_conservation():
    sim = Simulator(num_pieces=6, num_engines=2, num_stocks=2)
    before = total_value(sim.pieces, sim.allbank)
    sim.run(cycles=3)
    after = total_value(sim.pieces, sim.allbank)
    assert after > 0  # wealth should remain positive

def test_piece_immutability():
    from pieces import Piece
    p = Piece(1, value=50)
    p.period = "b"
    with pytest.raises(ValueError):
        p.set_value(60)
    with pytest.raises(ValueError):
        p.change_stock("STK1")

def test_council_transfer():
    from pieces import Piece
    from council import Council
    from allbank import AllBank

    p1, p2 = Piece(1, 100), Piece(2, 50)
    council = Council(AllBank())
    council.transfer_value(p1, p2, 25)
    assert p1.value == 75
    assert p2.value == 75
