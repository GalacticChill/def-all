class AllBank:
    def __init__(self):
        self.value = 0.0

    def deposit(self, amount: float):
        self.value += amount

    def withdraw(self, amount: float):
        if amount > self.value:
            raise ValueError("Insufficient all-bank funds")
        self.value -= amount
        return amount
