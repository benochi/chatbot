import requests
import json

# Connect to the Alpha Vantage API and request the data
url = "https://www.alphavantage.co/query"
params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": "AAPL",
    "apikey": "YOUR_API_KEY"
}
response = requests.get(url, params=params)
data = json.loads(response.content)

# Parse the data and get the latest closing price
time_series = data["Time Series (Daily)"]
latest_day = list(time_series.keys())[0]
latest_closing_price = float(time_series[latest_day]["4. close"])

# Perform analysis on the data (e.g. calculate moving averages)
# ...

# Output the analysis results
print(f"The latest closing price for AAPL is {latest_closing_price}")
