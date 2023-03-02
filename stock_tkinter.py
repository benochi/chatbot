import tkinter as tk
import requests

class StockBot:
    def __init__(self, symbol):
        self.symbol = symbol
        self.price = tk.StringVar()
        self.volume = tk.StringVar()
        self.update_data()
        
    def update_data(self):
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={self.symbol}&apikey=YOUR_API_KEY"
        data = requests.get(url).json()["Global Quote"]
        self.price.set(data["05. price"])
        self.volume.set(data["06. volume"])
        self.window.after(60000, self.update_data)
        
    def run(self):
        self.window = tk.Tk()
        self.window.title(f"StockBot: {self.symbol}")
        tk.Label(self.window, text="Price:").grid(row=0, column=0)
        tk.Label(self.window, textvariable=self.price).grid(row=0, column=1)
        tk.Label(self.window, text="Volume:").grid(row=1, column=0)
        tk.Label(self.window, textvariable=self.volume).grid(row=1, column=1)
        self.window.mainloop()

if __name__ == "__main__":
    bot = StockBot("AAPL")
    bot.run()
