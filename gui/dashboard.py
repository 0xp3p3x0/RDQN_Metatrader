import tkinter as tk

class Dashboard(tk.Frame):
    def __init__(self, master, bot):
        super().__init__(master)
        self.bot = bot
        self.init_ui()
    
    def init_ui(self):
        self.profit_label = tk.Label(self, text="Profit: $0")
        self.profit_label.pack()

        self.update_dashboard()

    def update_dashboard(self):
        profit = self.bot.get_profit()
        self.profit_label.config(text=f"Profit: ${profit:.2f}")
        self.after(1000, self.update_dashboard)  # Refresh every second
