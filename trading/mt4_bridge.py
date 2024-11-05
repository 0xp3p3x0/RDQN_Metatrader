import metatrader.mt4 as mt4

class MT4Bridge:
    def __init__(self):
        if not mt4.initialize():
            raise Exception("Failed to initialize MetaTrader")

    def place_order(self, symbol, volume, price, order_type):
        order_request = {
            "action": mt4.TRADE_ACTION_PENDING,
            "symbol": symbol,
            "volume": volume,
            "type": mt4.ORDER_TYPE_BUY_LIMIT,
            "price": price,
            "deviation": 10,
            "magic": 123456,
            "comment": "Grid Order",
        }
        mt4.order_send(order_request)
