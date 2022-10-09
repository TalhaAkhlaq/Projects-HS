#import modules
from select import KQ_FILTER_AIO
from polygon import RESTClient
import datetime as dt
import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot

# API Key
polygonAPIkey = 'Your API Key'

# Create a REST client object
# API key is required to use the REST client
client = RESTClient(polygonAPIkey) 

# Enter a stock ticker symbol
contractNames = []
for c in client.list_options_contracts(underlying_ticker = 'MSFT', limit = 1000):
    contractNames.append(c)
print(contractNames)
# Get the last 10 days of AAPL stock data
contractData = contractNames[398]
optionsTicker = contractData.ticker
dailyOptionData = client.get_aggs(ticker = optionsTicker, 
                                multiplier = 1,
                                timespan = 'day',
                                new_var = '1900-01-01',
                                to = '2100-01-01')

# Create a dataframe from the daily stock data

intradayOptionData = client.get_aggs(ticker = optionsTicker, 
                                     multiplier = 5,
                                     timespan = 'minute',
                                     new_var = '1900-01-01',
                                     to = '2100-01-01')
# Create a dataframe from the daily stock data
hourlyOptionData = client.get_aggs(ticker = optionsTicker, 
                                   multiplier = 2,
                                   timespan = 'hour',
                                   new_var = '1900-01-01',
                                   to = '2100-01-01')

# Create a dataframe from the daily stock data
optionDataFrame = pd.DataFrame(dailyOptionData)
optionDataFrame['Date'] = optionDataFrame['timestamp'].apply(
                          lambda x: pd.to_datetime(x*1000000))

# Create a dataframe from the daily stock data
optionDataFrame = optionDataFrame.set_index('Date')
fig = go.Figure(data=[go.Candlestick(x=optionDataFrame.index,
                open=optionDataFrame['open'],
                high=optionDataFrame['high'],
                low=optionDataFrame['low'],
                close=optionDataFrame['close'])])

# Plot the data
plot(fig, auto_open=True)