import pandas as pd
import numpy as np
import yfinance as yf
import datetime
import os

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)


class History():

    def __init__(self):
        self.stock = yf.Ticker("SPY")

    def summary(self):
        hist = self.stock.history(period = "1y")
        df = pd.DataFrame(hist)
        df = df.describe()
        return df

    def info(self):
        hist = self.stock.history(period = "1y")
        df = pd.DataFrame(hist)
        df = df.info()
        return df

    def dataframe(self):
        hist = self.stock.history(period = "1y")
        df = pd.DataFrame(hist)
        return df

    def day_to_day_difference(self):
        hist = self.stock.history(period = "1y")
        df = pd.DataFrame(hist)
        df1 = df
        df1["Open_diff"] = df["Open"] - df["Open"].shift(1)
        df1["Close_diff"] = df["Close"] - df["Close"].shift(1)
        df1["High_diff"] = df["High"] - df["High"].shift(1)
        df1["Low_diff"] = df["Low"] - df["Low"].shift(1)
        df1["Volume_diff"] = df["Volume"] - df["Volume"].shift(1)
        df1 = df1[["Open_diff", "Close_diff", "High_diff", "Low_diff", "Volume_diff"]]
        df1 = df1.dropna()
        return df1

    def describe_difference(self):
        hist = self.stock.history(period = "1y")
        df = pd.DataFrame(hist)
        df1 = df
        df1["Open_diff"] = df["Open"] - df["Open"].shift(1)
        df1["Close_diff"] = df["Close"] - df["Close"].shift(1)
        df1["High_diff"] = df["High"] - df["High"].shift(1)
        df1["Low_diff"] = df["Low"] - df["Low"].shift(1)
        df1["Volume_diff"] = df["Volume"] - df["Volume"].shift(1)
        df1 = df1[["Open_diff", "Close_diff", "High_diff", "Low_diff", "Volume_diff"]]
        df1 = df1.dropna()

        df1 = df1.describe()
        return df1

    def df_high_pos(self):
        hist = self.stock.history(period = "1y")
        df = pd.DataFrame(hist)
        df1 = df
        df1["Open_diff"] = df["Open"] - df["Open"].shift(1)
        df1["Close_diff"] = df["Close"] - df["Close"].shift(1)
        df1["High_diff"] = df["High"] - df["High"].shift(1)
        df1["Low_diff"] = df["Low"] - df["Low"].shift(1)
        df1["Volume_diff"] = df["Volume"] - df["Volume"].shift(1)
        df1 = df1[["Open_diff", "Close_diff", "High_diff", "Low_diff", "Volume_diff"]]
        df1 = df1.dropna()

        df1 = df[["High_diff"]]

        df1 = df1[df1["High_diff"] >= 0.0000]

        df1 = df1.describe()
        return df1

    def df_high_neg(self):
        hist = self.stock.history(period = "1y")
        df = pd.DataFrame(hist)
        df1 = df
        df1["Open_diff"] = df["Open"] - df["Open"].shift(1)
        df1["Close_diff"] = df["Close"] - df["Close"].shift(1)
        df1["High_diff"] = df["High"] - df["High"].shift(1)
        df1["Low_diff"] = df["Low"] - df["Low"].shift(1)
        df1["Volume_diff"] = df["Volume"] - df["Volume"].shift(1)
        df1 = df1[["Open_diff", "Close_diff", "High_diff", "Low_diff", "Volume_diff"]]
        df1 = df1.dropna()

        df1 = df[["High_diff"]]

        df1 = df1[df1["High_diff"] <= 0.0000]

        df1 = df1.describe()
        return df1

    def df_low_pos(self):
        hist = self.stock.history(period = "1y")
        df = pd.DataFrame(hist)
        df1 = df
        df1["Open_diff"] = df["Open"] - df["Open"].shift(1)
        df1["Close_diff"] = df["Close"] - df["Close"].shift(1)
        df1["High_diff"] = df["High"] - df["High"].shift(1)
        df1["Low_diff"] = df["Low"] - df["Low"].shift(1)
        df1["Volume_diff"] = df["Volume"] - df["Volume"].shift(1)
        df1 = df1[["Open_diff", "Close_diff", "High_diff", "Low_diff", "Volume_diff"]]
        df1 = df1.dropna()

        df1 = df[["Low_diff"]]

        df1 = df1[df1["Low_diff"] >= 0.0000]

        df1 = df1.describe()
        return df1

    def df_low_neg(self):
        hist = self.stock.history(period = "1y")
        df = pd.DataFrame(hist)
        df1 = df
        df1["Open_diff"] = df["Open"] - df["Open"].shift(1)
        df1["Close_diff"] = df["Close"] - df["Close"].shift(1)
        df1["High_diff"] = df["High"] - df["High"].shift(1)
        df1["Low_diff"] = df["Low"] - df["Low"].shift(1)
        df1["Volume_diff"] = df["Volume"] - df["Volume"].shift(1)
        df1 = df1[["Open_diff", "Close_diff", "High_diff", "Low_diff", "Volume_diff"]]
        df1 = df1.dropna()

        df1 = df[["Low_diff"]]

        df1 = df1[df1["Low_diff"] <= 0.0000]

        df1 = df1.describe()
        return df1

    def df_vol_pos(self):
        hist = self.stock.history(period = "1y")
        df = pd.DataFrame(hist)
        df1 = df
        df1["Open_diff"] = df["Open"] - df["Open"].shift(1)
        df1["Close_diff"] = df["Close"] - df["Close"].shift(1)
        df1["High_diff"] = df["High"] - df["High"].shift(1)
        df1["Low_diff"] = df["Low"] - df["Low"].shift(1)
        df1["Volume_diff"] = df["Volume"] - df["Volume"].shift(1)
        df1 = df1[["Open_diff", "Close_diff", "High_diff", "Low_diff", "Volume_diff"]]
        df1 = df1.dropna()

        df1 = df[["Volume_diff"]]

        df1 = df1[df1["Volume_diff"] >= 0.0000]

        df1 = df1.describe()
        return df1

    def df_vol_neg(self):
        hist = self.stock.history(period = "1y")
        df = pd.DataFrame(hist)
        df1 = df
        df1["Open_diff"] = df["Open"] - df["Open"].shift(1)
        df1["Close_diff"] = df["Close"] - df["Close"].shift(1)
        df1["High_diff"] = df["High"] - df["High"].shift(1)
        df1["Low_diff"] = df["Low"] - df["Low"].shift(1)
        df1["Volume_diff"] = df["Volume"] - df["Volume"].shift(1)
        df1 = df1[["Open_diff", "Close_diff", "High_diff", "Low_diff", "Volume_diff"]]
        df1 = df1.dropna()

        df1 = df[["Volume_diff"]]

        df1 = df1[df1["Volume_diff"] <= 0.0000]

        df1 = df1.describe()
        return df1


hist = History()
##print(hist.summary())
##print(hist.info())
##print(hist.dataframe())

##print(hist.day_to_day_difference())

##print(hist.describe_difference())

print("High Posative \n", round(hist.df_high_pos(), 2), "\n")

print("High Negative \n", round(hist.df_high_neg(), 2), "\n")

print("Low Positive \n", round(hist.df_low_pos(), 2), "\n")

print("Low Negative \n", round(hist.df_low_neg(), 2), "\n")


##
##def summ():
##    tick = yf.Ticker("SPY")
##    hist = tick.history(period="1y")
##    df = pd.DataFrame(hist).describe()
##    return df
##
##print(summ())
