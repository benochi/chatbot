import yfinance as yf
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def get_stock_price(stock_name):
    stock = yf.Ticker(stock_name)
    return stock.info['regularMarketPrice']

def get_stock_history(stock_name):
    stock = yf.Ticker(stock_name)
    return stock.history(period="max")

def display_stock_price():
    stock_name = entry.get()
    data = yf.Ticker(stock_name)
    price = data.history(period='1d')['Close'][0]
    price_text.set(f"Current Price: ${price:.2f}")

def display_stock_graph():
    stock_name = entry.get()
    history = get_stock_history(stock_name)
    fig = Figure(figsize=(5, 4), dpi=100)
    subplot = fig.add_subplot(111)
    subplot.plot(history.index, history["Close"])
    subplot.set_title(f"{stock_name} Stock Price History")
    subplot.set_xlabel("Date")
    subplot.set_ylabel("Price ($)")
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=3, column=0, columnspan=2)

root = tk.Tk()
root.geometry("600x600")
root.title("Stock Bot")

label = tk.Label(root, text="Enter stock name:")
label.grid(row=0, column=0)

entry = tk.Entry(root)
entry.grid(row=0, column=1)

price_text = tk.StringVar()
price_label = tk.Label(root, textvariable=price_text)
price_label.grid(row=1, column=0, columnspan=2)

price_button = tk.Button(root, text="Get Current Price", command=display_stock_price)
price_button.grid(row=2, column=0)

graph_button = tk.Button(root, text="Display Price History", command=display_stock_graph)
graph_button.grid(row=2, column=1)

root.mainloop()
