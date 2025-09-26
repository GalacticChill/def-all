from simulator import Simulator

if __name__ == "__main__":
    sim = Simulator(num_pieces=10, num_engines=2, num_stocks=3)
    sim.run(cycles=5)
