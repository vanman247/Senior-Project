import pandas as pd
import numpy as np
import yfinance as yf
import datetime
import os

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

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

class Stock:

    def __init__(self):
        self.stock = yf.Ticker("SPY")

    def current_price(self):
        self.hist = self.stock.history(period = "1d")
        self.df = pd.DataFrame(self.hist)
        self.close = round(self.df[["Close"]].iloc[0], 2)
        return self.close.iloc[0]

## Call the Classes
chain = Chain()
stock = Stock()

## Set the Expiration date
exp_date = str(chain.next_friday())

## Import Option Chain Data of Stock(SPY)
opt = chain.opt(exp_date)

## Seperate database into Calls and Puts
calls = chain.calls(opt)

puts = chain.puts(opt)

## Run Bull and Bear Call Spread
cp = stock.current_price()


"""
Strike: This column shows the price at which a call buyer can purchase the security if the option is exercised.
In the case of a put option, it’s the price at which the option buyer can sell the underlying security should the option be exercised.
On the flip side, an option writer will be assigned to produce the underlying security at the strike price if an option he or she sells (writes) is exercised.

contractSymbol: This element of the options table contains the information for which option you are looking at; it can be broken down into a few major sections.
Figure 4 shows what is contained in the symbol.

LastTradeDate: The price of the last trade that went through.

Chg (Change) : Change is how much the Last price has changed since the previous close.

Bid: The price at which buyers are trying to buy the option. If you market sell an option, you’ll typically get this price assuming instant execution.
This is the price for one share. Since one option is for 100 shares, to get the cost of an option you must multiply this price by 100.

Ask: The price at which sellers are trying to sell the option. If you market buy an option, you’ll typically get this price assuming instant execution.
This is the price for one share. Since one option is for 100 shares, to get the cost of an option you must multiply this price by 100.

Vol (Volume): Lets you know how many contracts have been traded during the session.
Options that have large volume typically have a tighter Bid-Ask spread since more traders are looking to get in and out of positions.

Open Int (Interest): The number of open positions in the contract that have not yet been offset.

"""

calls = calls[["strike", "bid", "ask"]]

calls["dif_prem"] = calls["ask"] - calls["bid"].shift(-1)

calls = calls[calls["strike"] >= cp]

##calls = calls[calls["dif_prem"] <= 0.1000]

avg_prem = round(calls["dif_prem"].mean(), 2)

##print(round(calls["dif_prem"].mean(), 2))
##
##calls = calls[calls["bid"] >= 0.01]
##
##calls = calls[calls["dif_prem"] >= avg_prem]
##
##calls = calls[calls["dif_prem"] >= 0.0125]
##
print(calls)
##
##print(cp)

