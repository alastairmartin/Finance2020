import yfinance as yf
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

ticker = yf.Ticker("VOD")
print(ticker)

print('-----------------------------------------------------------------------------')
# get stock info
# print('*** Info: ',ticker.info)

try:
    ticker.info
    for x,y in ticker.info.items():
        print(x,': ',y)
except Exception as e:
    print(e)

print('History ---------------------------------------------------------------------')
# get historical market data
try:
    prices = ticker.history(period="1y",interval='1d' ) #pandas dataframe
    print('*** History: ', prices)
except Exception as e:
    print(e)

print('Action-----------------------------------------------------------------------')
# show actions (dividends, splits)
try:
    print('*** Actions: ',ticker.actions)
except Exception as e:
    print(e)
       
print('Dividends -------------------------------------------------------------------')
# show dividends
try:
    print('*** Dividends',ticker.dividends)
except Exception as e:
    print(e)

print('Splits ----------------------------------------------------------------------')
# show splits
try:
    print('*** Splits',ticker.splits)
except Exception as e:
    print(e)

print('Financials ------------------------------------------------------------------')
# show financials
try:
    print('*** Financials: ',ticker.financials)
except Exception as e:
        print(e)

try:
    print('*** Quarterly financials: ',ticker.quarterly_financials)
except Exception as e:
    print(e)

print('Major holders ---------------------------------------------------------------')
# show major holders
try:
    print('*** Major holders: ',ticker.major_holders)
except Exception as e:
    print(e)

print('-----------------------------------------------------------------------------')
# show institutional holders
try:
    print('*** Institutional holders: ',ticker.institutional_holders)
except Exception as e:
        print(e)

print('Balance Sheet ---------------------------------------------------------------')
# show balance sheet
try:
    print('*** Balance sheet: ',ticker.balance_sheet)
except Exception as e:
    print(e)
try:
    print('*** Quarterly balance sheet: ',ticker.quarterly_balance_sheet)
except Exception as e:
    print(e)


print('Cashflow --------------------------------------------------------------------')
# show cashflow
try:
    print('*** Cashflow: ',ticker.cashflow)
except Exception as e:
    print(e)
try:
    print('*** Quarterly cashflow: ',ticker.quarterly_cashflow)
except Exception as e:
    print(e)

print('Earnings --------------------------------------------------------------------')
# show earnings
try:
    print('*** Earnings: ',ticker.earnings)
except Exception as e:
    print(e)
try:
    print('*** Quarterly earnings: ',ticker.quarterly_earnings)
except Exception as e:
    print(e)

print('Sustainability --------------------------------------------------------------')
# show sustainability
try:
    print('*** Sustainability: ',ticker.sustainability)
except Exception as e:
    print(e)

print('-----------------------------------------------------------------------------')
# show analysts recommendations
try:
    print('*** Recommendations: ',ticker.recommendations)
except Exception as e:
    print(e)

print('-----------------------------------------------------------------------------')
# show next event (earnings, etc)
try:
    print('*** Calendar: ',ticker.calendar)
except Exception as e:
    print(e)

print('-----------------------------------------------------------------------------')
# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
try:
    print('*** ISIN: ',ticker.isin)
except Exception as e:
    print(e)

# show options expirations
#print(ticker.options)

# get option chain for specific expiration
#opt = ticker.option_chain('YYYY-MM-DD')
# data available via: opt.calls, opt.puts