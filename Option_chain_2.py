import pandas as pd
import numpy as np
import yfinance as yf
import datetime
import os

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)


stock = yf.Ticker("SPY")
today = datetime.date.today()

experation_date = stock.options

print(experation_date)

opt = stock.option_chain()
call = opt.calls
calls = pd.DataFrame(call)
