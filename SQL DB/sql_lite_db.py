import pandas as pd
import numpy as np
import sqlite3
import yfinance as yf
from datetime import date

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

def make_db():
    conn = sqlite3.connect("SPY.db")
    c = conn.cursor()
    conn.commit()
    return conn, c

def add_calls_table(conn, c):
    stock = yf.Ticker("SPY")
    des = list(stock.options)
    next_exp_date = des[0]
    title = str(des[0]).replace("-", "_")
    calls = stock.option_chain(next_exp_date).calls
    today = str(date.today()).replace("-", "_")
    c.execute('CREATE TABLE IF NOT EXISTS calls_{}_exp_{} (contractSymbol,lastTradeDate,strike,lastPrice,bid,ask,change,percentChange,volume,openInterest,impliedVolatility,inTheMoney,contractSize,currency)'.format(today, title))
    conn.commit()
    df = calls.to_sql("calls_{}_exp_{}".format(today, title), con=conn, if_exists='replace', index=False)
    conn.commit()
    return

def add_puts_table(conn, c):
    stock = yf.Ticker("SPY")
    des = list(stock.options)
    next_exp_date = des[0]
    title = str(des[0]).replace("-", "_")
    calls = stock.option_chain(next_exp_date).puts
    today = str(date.today()).replace("-", "_")
    c.execute('CREATE TABLE IF NOT EXISTS puts_{}_exp_{} (contractSymbol,lastTradeDate,strike,lastPrice,bid,ask,change,percentChange,volume,openInterest,impliedVolatility,inTheMoney,contractSize,currency)'.format(today, title))
    conn.commit()
    df = calls.to_sql("puts_{}_exp_{}".format(today, title), con=conn, if_exists='replace', index=False)
    conn.commit()
    return

conn, c = make_db()
add_calls_table(conn, c)
add_puts_table(conn, c)
