import yfinance as yf

ticker = yf.Ticker("BA.L")
print(ticker)

print('-----------------------------------------------------------------------------')
# get stock info
print('*** Info: ',ticker.info)
for x,y in ticker.info.items():
    print(x,': ',y)

print('-----------------------------------------------------------------------------')
# get historical market data
print('*** History: ',ticker.history(period="5yr",interval='1h'))

print('-----------------------------------------------------------------------------')
# show actions (dividends, splits)
print('*** Actions: ',ticker.actions)

print('-----------------------------------------------------------------------------')
# show dividends
print('*** Dividends',ticker.dividends)

print('-----------------------------------------------------------------------------')
# show splits
print('*** Splits',ticker.splits)

print('-----------------------------------------------------------------------------')
# show financials
print('*** Financials: ',ticker.financials)
print('*** Quarterly financials: ',ticker.quarterly_financials)

print('-----------------------------------------------------------------------------')
# show major holders
print('*** Major holders: ',ticker.major_holders)

print('-----------------------------------------------------------------------------')
# show institutional holders
print('*** Institutional holders: ',ticker.institutional_holders)

print('-----------------------------------------------------------------------------')
# show balance heet
print('*** Balance sheet: ',ticker.balance_sheet)
print('*** Quarterly balance sheet: ',ticker.quarterly_balance_sheet)

print('-----------------------------------------------------------------------------')
# show cashflow
print('*** Cashflow: ',ticker.cashflow)
print('*** Quarterly cashflow: ',ticker.quarterly_cashflow)

print('-----------------------------------------------------------------------------')
# show earnings
print('*** Earnings: ',ticker.earnings)
print('*** Quarterly earnings: ',ticker.quarterly_earnings)

print('-----------------------------------------------------------------------------')
# show sustainability
print('*** Sustainability: ',ticker.sustainability)

print('-----------------------------------------------------------------------------')
# show analysts recommendations
print('*** Recommendations: ',ticker.recommendations)

print('-----------------------------------------------------------------------------')
# show next event (earnings, etc)
print('*** Calendar: ',ticker.calendar)

print('-----------------------------------------------------------------------------')
# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
print('*** ISIN: ',ticker.isin)

# show options expirations
#print(ticker.options)

# get option chain for specific expiration
#opt = ticker.option_chain('YYYY-MM-DD')
# data available via: opt.calls, opt.puts