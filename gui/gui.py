import tkinter as tk
from gui.dashboard import Dashboard
from gui.settings import Settings
from trading.grid_trading import GridTradingBot

class TradingBotGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Grid Trading Bot")
        self.bot = GridTradingBot()  # Initialize trading bot
        self.setup_gui()
    
    def setup_gui(self):
        settings_frame = Settings(self.window, self.bot)
        settings_frame.pack(side=tk.LEFT)

        dashboard_frame = Dashboard(self.window, self.bot)
        dashboard_frame.pack(side=tk.RIGHT)
        
        start_button = tk.Button(self.window, text="Start Trading", command=self.start_bot)
        start_button.pack(side=tk.BOTTOM)

        stop_button = tk.Button(self.window, text="Stop Trading", command=self.stop_bot)
        stop_button.pack(side=tk.BOTTOM)

    def start_bot(self):
        self.bot.start_trading()

    def stop_bot(self):
        self.bot.stop_trading()
    
    def run(self):
        self.window.mainloop()
