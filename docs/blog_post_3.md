# Blog Post 3

## Thoughts on what to do next

We need to develop a way to get a "Snap-shot" of Options Data. Now this is a "Quick and Dirty" way to look at the data and get a feel for what the data is saying before we take any steps further.

### Step 1

First, we will need to import the necessary python libraries.

    # Importing Libraries
    
    2.    import pandas as pd
    3.    import numpy as np
    4.    import yfinance as yf
    5.    import datetime
    6.    import os
    7.    import sqlite3

### Step 2

After importing the libraries next you need to do is pull in the Option Data. So, for this I decided to go down the path of using Classes. Now I chose this because I wanted to develop my grasp of Classes within Python and because there were several attributes that Options have.
    
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
            
The Function "next_friday()" calculates the if the date of the Upcoming Fiday. *Disclaimer: If the Current Day is a Friday, then it will so the same date as the "next_friday()" function.*
 
The "Opt()" Function does the bulk of the work in calling and collecting the Options Chains.
 
The "Calls()" Function pulls out the Calls of the Options from the "Opt()" Function.
 
The "Puts()" Function pulls out the Puts of the Options from the "Opt()" Function.
 
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

### Step 4

Now we need to call Both the Chain and Stock Classes. Then call each of the attributes of the Chain Class and the Stock Class.
    
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

## Step 5
Next, we now need to make a subset of the Dataset of the Strike Price, Bid and Ask. Once that is made, we then need to calculate the premium from between Ask and Bid at different Strike Prices. then you will need to filter the new dataset to include only those strike prices that are greater than or equal to the Current Stock Price of the underlying stock. Then we need to round the Premium to the 2nd decimal place. The reason for this is that because if the US dollar only goes out to 2 decimals places.

    calls = calls[["strike", "bid", "ask"]]

    calls["dif_prem"] = calls["ask"] - calls["bid"].shift(-1)

    calls = calls[calls["strike"] >= cp]

    avg_prem = round(calls["dif_prem"].mean(), 2)
    
We now have our "Quick and Dirty" Dataset for Running Bull Call Spreads.
