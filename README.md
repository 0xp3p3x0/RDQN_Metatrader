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


Setup and Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/GridTradingBot.git
cd GridTradingBot
Install dependencies:

bash
Copy code
pip install -r requirements.txt
MetaTrader 4 Setup:

Ensure MetaTrader 4 is installed and configured on your machine.
Set up the MetaTrader5 library for Python and make sure your MT4 terminal is properly configured to allow external API requests.
Usage
Run the GUI:

bash
Copy code
python main.py
Adjust Parameters:

Use the Settings Panel to adjust grid trading parameters (grid levels, grid spacing, lot size, etc.).
Start or stop the bot through the GUI controls.
Monitor Performance:

The Dashboard Panel will display real-time performance metrics, including profit/loss and open positions.
A log file records bot actions and any errors encountered.
Backtesting (optional):

Use the utils/backtester.py file to test the bot on historical data. Modify backtester.py to specify the data and parameters for testing.
Configuration
Configuration options are located in config.py. Key settings include:

Grid Trading Parameters:

GRID_LEVELS: Number of grid levels to maintain.
GRID_SPACING_PIPS: Spacing between each grid level in pips.
LOT_SIZE: Lot size for each trade.
SYMBOL: The currency pair or symbol to trade (e.g., "EURUSD").
RISK_MANAGEMENT: Risk parameters such as max drawdown and capital per trade.
Rainbow DQN Parameters:

gamma: Discount factor for future rewards.
learning_rate: Learning rate for the DQN.
batch_size: Batch size for training.
buffer_size: Size of the experience replay buffer.
Customize these values based on your trading goals and risk tolerance.

How It Works
Grid Trading Strategy: The bot places multiple buy-limit orders at specified grid levels below the current price. These levels are spaced at fixed intervals, based on the configured grid spacing, to capture opportunities during mean-reversion movements.

Rainbow DQN Model: The model leverages Rainbow DQN to make dynamic adjustments to grid parameters. It learns from market data, optimizing the bot’s ability to capture profitable trades within a mean-reverting environment.

MetaTrader 4 Integration: The bot uses MetaTrader5 Python library to communicate with the MT4 platform, execute orders, and retrieve real-time market data.

GUI Control: The GUI (using Tkinter) provides control over the bot's operations, allowing users to start, stop, and adjust settings in real time. The Dashboard displays live performance metrics, including profit, order history, and grid levels.

Screenshots
Main GUI Interface
Settings Panel: Configure grid trading parameters.
Dashboard Panel: Displays profit/loss, open positions, and trade history.
Performance Dashboard
Track trading performance metrics in real time.
Contributing
Contributions are welcome! Please open an issue to discuss changes or create a pull request for any improvements or bug fixes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Special thanks to the open-source community and resources that made this project possible, especially the MetaTrader5 library and reinforcement learning frameworks that enabled advanced trading strategies with Python.