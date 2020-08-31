import yfinance as yf

msft = yf.Ticker("MSFT")
print(msft)
"""
returns
<yfinance.Ticker object at 0x1a1715e898>
"""

# get stock info
print('*** Info: ',msft.info)


# get historical market data
print('*** History: ',msft.history(period="1wk",interval='5m'))

# show actions (dividends, splits)
print('*** Actions: ',msft.actions)

# show dividends
print('Dividends',msft.dividends)

# show splits
print('Splits',msft.splits)

# show quarterly financials
print(msft.quarterly_financials)