import tkinter as tk
from config import GRID_LEVELS, GRID_SPACING_PIPS, LOT_SIZE

class Settings(tk.Frame):
    def __init__(self, master, bot):
        super().__init__(master)
        self.bot = bot
        
        tk.Label(self, text="Grid Levels").pack()
        self.grid_levels = tk.IntVar(value=GRID_LEVELS)
        tk.Entry(self, textvariable=self.grid_levels).pack()

        tk.Label(self, text="Grid Spacing (pips)").pack()
        self.grid_spacing = tk.IntVar(value=GRID_SPACING_PIPS)
        tk.Entry(self, textvariable=self.grid_spacing).pack()

        tk.Label(self, text="Lot Size").pack()
        self.lot_size = tk.DoubleVar(value=LOT_SIZE)
        tk.Entry(self, textvariable=self.lot_size).pack()

        tk.Button(self, text="Apply", command=self.apply_settings).pack()
    
    def apply_settings(self):
        # Apply settings to the bot
        self.bot.update_parameters(
            grid_levels=self.grid_levels.get(),
            grid_spacing=self.grid_spacing.get(),
            lot_size=self.lot_size.get()
        )
