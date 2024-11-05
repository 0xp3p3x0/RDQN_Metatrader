# config.py

# Grid Trading Configurations
GRID_LEVELS = 5
GRID_SPACING_PIPS = 10
LOT_SIZE = 0.1
TAKE_PROFIT_PIPS = 20
SYMBOL = "EURUSD"
RISK_MANAGEMENT = {
    "max_drawdown": 0.1,  # Maximum allowed drawdown
    "capital_per_trade": 0.05,  # Capital allocated per trade
}

# DQN Configurations
DQN_CONFIG = {
    "gamma": 0.99,
    "learning_rate": 0.001,
    "batch_size": 64,
    "buffer_size": 10000,
    "update_target_every": 1000,
}
