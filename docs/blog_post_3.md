# Blog Post 3

## Thoughts on what to do next

We need to develop a way to get a "Snap-shot" of Options Data. Now this is a "Quick and Dirty" way to look at the data and get a feel for what the data is saying before we take any steps further.

### Step 1

First we will need to import the necessary python libraries.

    # Importing Libraries
    
    2.    import pandas as pd
    3.    import numpy as np
    4.    import yfinance as yf
    5.    import datetime
    6.    import os
    7.    import sqlite3

### Step 2

After importing the libraries next you need to do is pull in the Option Data. So for this I decided to go down the path of using Classes. Now I chose this because I wanted to develop my grasp of Classes within Python and because there were several attributes that Options have.
    
    class Chain:

        def __init__(self):
            self.stock = yf.Ticker("SPY")
            self.d = datetime.date.today()

        def next_friday(self):
            self.d = datetime.date.today()
            while self.d.weekday() != 4:
                self.d += datetime.timedelta(1)
            return self.d

        def opt(self, exp_date):
            self.opt = self.stock.option_chain(exp_date)
            return self.opt

        def calls(self, opt):
            self.call = self.opt.calls
            self.calls = pd.DataFrame(self.call)
            return self.calls

        def puts(self, opt):
            self.put = self.opt.puts
            self.puts = pd.DataFrame(self.put)
            return self.puts
            
The Function "next_friday()" calculates the if the date of the Upcoming Fiday. *Disclaimer: If the Current Day is a Friday then it will so the same date as the "next_friday()" function.*
 
The "Opt()" Function does the bulk of the work in calling and collecting the Options Chains.
 
The "calls()" Function pulls out the Calls of the Options from the "Opt" Function.
 
The "puts()" Function pulls out the Puts of the Options from the "Opt" Function.
 
 ### Step 3
 
 We now need to know what is the Current Price of the Stock.

    class Stock:

        def __init__(self):
            self.stock = yf.Ticker("SPY")

        def current_price(self):
            self.hist = self.stock.history(period = "1d")
            self.df = pd.DataFrame(self.hist)
            self.close = round(self.df[["Close"]].iloc[0], 2)
            return self.close.iloc[0]
