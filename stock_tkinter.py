import yfinance as yf
import matplotlib.pyplot as plt
from tkinter import *

# Define the function to retrieve the stock data and display the graph
def get_stock_data():
    # Get the stock symbol entered by the user
    symbol = stock_symbol.get()

    # Use yfinance to retrieve the stock data
    stock = yf.Ticker(symbol)
    data = stock.history(period="max")

    # Plot the closing price data as a line graph
    plt.plot(data['Close'])
    plt.title(symbol)
    plt.xlabel('Date')
    plt.ylabel('Price')

    # Display the graph in the Matplotlib window
    plt.show()

# Create the main window
root = Tk()
root.title("Stock Bot")

# Create a label for the stock symbol entry
symbol_label = Label(root, text="Enter Stock Symbol:")
symbol_label.pack()

# Create an entry for the stock symbol
stock_symbol = Entry(root)
stock_symbol.pack()

# Create a button to retrieve the stock data and display the graph
get_data_button = Button(root, text="Get Stock Data", command=get_stock_data)
get_data_button.pack()

# Run the main loop
root.mainloop()
