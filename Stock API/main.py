import requests
import time

# API Key
# https://twelvedata.com/
# https://twelvedata.com/pricing

ticker = "MSFT"
api_key = "4e61eafd710346478686d7eda5415321"

# Main
# print(get_stock_price(ticker, api_key))
# print(get_stock_quote(ticker, api_key))

def get_stock_price(ticker_symbol, api):
    url = f"https://api.twelvedata.com/price?symbol={ticker_symbol}&apikey={api}"
    response = requests.get(url).json()
    price = response['price'][:-3]
    return price

# Path: Stock API\main.py
# Compare this snippet from main.py:


def get_stock_quote(ticker_symbol, api):
    url = f"https://api.twelvedata.com/quote?symbol={ticker_symbol}&apikey={api}"
    response = requests.get(url).json()
    return response


# Path: Stock API\main.py
# Compare this snippet from main.py:
# if hands:
# for hand in hands:
# drawing_utils.draw_landmarks(frame, hand)
# for id, lm in enumerate(hand.landmark):

stockdata = get_stock_quote(ticker, api_key)
stock_price = get_stock_price(ticker, api_key)

# exchange = stockdata['exchange']
# currency = stockdata['currency']
# open_price = stockdata['open']
# high_price = stockdata['high']
# low_price = stockdata['low']
# close_price = stockdata['close']
# volume = stockdata['volume']
name = stockdata['name']

print(name, stock_price)