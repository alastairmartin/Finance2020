import yfinance as yf

msft = yf.Ticker("BA.L")
print(msft)
"""
returns
<yfinance.Ticker object at 0x1a1715e898>
"""

print('-----------------------------------------------------------------------------')
# get stock info
print('*** Info: ',msft.info)
for x,y in msft.info.items():
    print(x,': ',y)

print('-----------------------------------------------------------------------------')
# get historical market data
print('*** History: ',msft.history(period="5yr",interval='1h'))

print('-----------------------------------------------------------------------------')
# show actions (dividends, splits)
print('*** Actions: ',msft.actions)

print('-----------------------------------------------------------------------------')
# show dividends
print('*** Dividends',msft.dividends)

print('-----------------------------------------------------------------------------')
# show splits
print('*** Splits',msft.splits)

print('-----------------------------------------------------------------------------')
# show financials
print('*** Financials: ',msft.financials)
print('*** Quarterly financials: ',msft.quarterly_financials)

print('-----------------------------------------------------------------------------')
# show major holders
print('*** Major holders: ',msft.major_holders)

print('-----------------------------------------------------------------------------')
# show institutional holders
print('*** Institutional holders: ',msft.institutional_holders)

print('-----------------------------------------------------------------------------')
# show balance heet
print('*** Balance sheet: ',msft.balance_sheet)
print('*** Quarterly balance sheet: ',msft.quarterly_balance_sheet)

print('-----------------------------------------------------------------------------')
# show cashflow
print('*** Cashflow: ',msft.cashflow)
print('*** Quarterly cashflow: ',msft.quarterly_cashflow)

print('-----------------------------------------------------------------------------')
# show earnings
print('*** Earnings: ',msft.earnings)
print('*** Quarterly earnings: ',msft.quarterly_earnings)

print('-----------------------------------------------------------------------------')
# show sustainability
print('*** Sustainability: ',msft.sustainability)

print('-----------------------------------------------------------------------------')
# show analysts recommendations
print('*** Recommendations: ',msft.recommendations)

print('-----------------------------------------------------------------------------')
# show next event (earnings, etc)
print('*** Calendar: ',msft.calendar)

print('-----------------------------------------------------------------------------')
# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
print('*** ISIN: ',msft.isin)

# show options expirations
#print(msft.options)

# get option chain for specific expiration
#opt = msft.option_chain('YYYY-MM-DD')
# data available via: opt.calls, opt.puts