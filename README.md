# Grid Trading Bot with Rainbow DQN for MetaTrader 4

This project is a buy-only grid trading bot using a **Rainbow DQN** model integrated with **MetaTrader 4** (MT4). It leverages a mean-reversion strategy and uses limit orders to establish a grid system, with the goal of optimizing trading returns. The bot is built with Python, featuring a GUI for real-time control and monitoring, and can be configured for both backtesting and live trading.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [How It Works](#how-it-works)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Grid Trading Strategy**: Implements a buy-only grid system to capture mean-reversion opportunities.
- **Rainbow DQN Model**: Integrates a deep Q-learning model (Rainbow DQN) to make decisions on grid spacing and levels.
- **GUI Control**: Real-time control panel with adjustable parameters, performance dashboard, and order history.
- **MetaTrader 4 Integration**: Communicates with MT4 for real-time order execution and monitoring.
- **Backtesting Support**: Test the strategy on historical data before deploying live.
- **Logging and Error Handling**: Logs system activity and handles errors to ensure stable operation.

---

## Project Structure

```plaintext
project_root/
│
├── main.py                     # Main entry point for the project
├── config.py                   # Configuration settings for the bot
├── requirements.txt            # Required libraries
│
├── gui/                        # GUI components
│   ├── gui.py                  # Main GUI application
│   ├── dashboard.py            # Dashboard to display performance metrics
│   └── settings.py             # GUI settings and parameter controls
│
├── model/                      # DQN Model files
│   ├── dqn.py                  # Rainbow DQN model implementation
│   ├── experience_replay.py    # Experience Replay Buffer
│   └── utils.py                # DQN training utilities and functions
│
├── trading/                    # MT4 Trading functionalities
│   ├── grid_trading.py         # Buy-only grid trading logic
│   ├── mt4_bridge.py           # MT4-Python bridge for order execution
│   └── mean_reversion.py       # Mean-reversion signal calculation
│
├── utils/                      # Utility functions
│   ├── data_utils.py           # Data fetching and preprocessing
│   ├── logger.py               # Logging utility
│   └── backtester.py           # Backtesting functionality for strategy validation
│
└── tests/                      # Testing scripts
    ├── test_model.py           # Test scripts for DQN model
    ├── test_trading.py         # Test scripts for trading functions
    └── test_gui.py             # Test scripts for GUI elements
