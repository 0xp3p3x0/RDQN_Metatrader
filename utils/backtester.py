class Backtester:
    def __init__(self, data, strategy):
        self.data = data
        self.strategy = strategy

    def run(self):
        for price in self.data:
            self.strategy.place_grid_orders(price)
            # Evaluate profit/loss based on historical data
