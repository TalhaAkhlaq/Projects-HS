from yahoo_fin.stock_info import *

stock = input("Enter a stock ticker: ")
portfolio = ('AAPL')
portfolio2 = ('MSFT')
portfolio3 = ('AMZN')
portfolio4 = ('GOOG')
portfolio5 = ('FB')

print (get_data(stock))
print (get_data(portfolio))
print (get_data(portfolio2))
print (get_data(portfolio3))
print (get_data(portfolio4))


