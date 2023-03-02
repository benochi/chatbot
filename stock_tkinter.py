import yfinance as yf
import tkinter as tk

def retrieve_data():
    ticker = e1.get()
    data = yf.Ticker(ticker)
    price = data.history(period='1d')['Close'][0]
    e2.delete(0, tk.END)
    e2.insert(0, str(price))

root = tk.Tk()
root.geometry('300x200')
root.title('StockBot')

label1 = tk.Label(root, text='Enter ticker symbol:')
label1.pack()

e1 = tk.Entry(root)
e1.pack()

button = tk.Button(root, text='Get Price', command=retrieve_data)
button.pack()

label2 = tk.Label(root, text='Price:')
label2.pack()

e2 = tk.Entry(root)
e2.pack()

root.mainloop()
