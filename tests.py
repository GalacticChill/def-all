#ol       ,  .       .,
# tests.py

from pieces import Piece
from engines import Engine
from stocks import Market
from council import Council
from allbank import AllBank

def test_total_value_invariant(engines, allbank):
    """
    Total value in system = sum(piece values) + AllBank balance
    Should remain constant if no new money is injected.
    """
    total_piece_value = sum(p.value for e in engines for p in e.pieces)
    total_value = total_piece_value + allbank.balance
    return total_value

def test_no_negative_piece_value(engines):
    """Ensure no piece has negative value."""
    for e in engines:
        for p in e.pieces:
            assert p.value >= 0, f"Piece {p.id} has negative value {p.value}"

def test_allbank_non_negative(allbank):
    """Ensure AllBank balance is never negative."""
    assert allbank.balance >= 0, f"AllBank has negative balance {allbank.balance}"

def test_piece_counts(engines):
    """Ensure no engine has zero pieces if rules prevent it."""
    for e in engines:
        assert len(e.pieces) >= 1, f"{e.name} has zero pieces"

def run_basic_tests(engines, council):
    print("Running basic invariants tests...")

    total = test_total_value_invariant(engines, council.allbank)
    print(f"Total system value: {total:.2f}")

    test_no_negative_piece_value(engines)
    print("No negative piece values ✅")

    test_allbank_non_negative(council.allbank)
    print("AllBank non-negative ✅")

    test_piece_counts(engines)
    print("Piece counts valid ✅")

    print("All basic tests passed!\n")


if __name__ == "__main__":
    # Sample setup for testing
    market = Market(["AAPL", "TSLA", "MSFT"])
    pieces1 = [Piece(id=i, value=100.0) for i in range(3)]
    pieces2 = [Piece(id=i+100, value=200.0) for i in range(2)]
    engine1 = Engine("Engine_1", pieces1, market)
    engine2 = Engine("Engine_2", pieces2, market)

    council = Council()
    engines = [engine1, engine2]

    # Run the tests
    run_basic_tests(engines, council)
