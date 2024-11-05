from trading.mt4_bridge import MT4Bridge
from config import GRID_LEVELS, GRID_SPACING_PIPS, LOT_SIZE, SYMBOL

class GridTradingBot:
    def __init__(self):
        self.mt4 = MT4Bridge()
        self.active_orders = []
        self.grid_levels = GRID_LEVELS
        self.grid_spacing = GRID_SPACING_PIPS

    def place_grid_orders(self, base_price):
        for i in range(1, self.grid_levels + 1):
            order_price = base_price - (i * self.grid_spacing)
            self.place_buy_order(order_price)

    def place_buy_order(self, price):
        order = {
            "symbol": SYMBOL,
            "volume": LOT_SIZE,
            "price": price,
            "type": "BUY_LIMIT",
        }
        self.mt4.place_order(**order)
