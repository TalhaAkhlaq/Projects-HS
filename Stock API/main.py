#import modules
from polygon import RESTClient
import datetime as dt
import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot

# API Key
polygonAPIkey = 'YOUR API KEY HERE'

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
dailyOptionData = client.getaggs(ticker = optionsTicker, 
                                  multiplier = 1,
                                  timespan = 'day',
                                  from = '1900-01-01',
                                  to = '2100-01-01')

# Create a dataframe from the daily stock data

intradayOptionData = client.getaggs(ticker = optionsTicker, 
                                     multiplier = 5,
                                     timespan = 'minute',
                                     from = '1900-01-01',
                                     to = '2100-01-01')
# Create a dataframe from the daily stock data
hourlyOptionData = client.getaggs(ticker = optionsTicker, 
                                   multiplier = 2,
                                   timespan = 'hour',
                                   from = '1900-01-01',
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
