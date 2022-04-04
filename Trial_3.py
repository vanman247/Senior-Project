import pandas as pd
import numpy as np
import yfinance as yf
import datetime
import os
import sqlite3

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

def stock(url):
    stock = yf.Ticker(url)
    return stock

def exp_dates(stock):
    des = list(stock.options)
    next_exp_date = des[0]
    print(next_exp_date)
    return next_exp_date
    
def create_calls_database():
    conn = sqlite3.connect('SPY.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS calls (contractSymbol,lastTradeDate,strike,lastPrice,bid,ask,change,percentChange,volume,openInterest,impliedVolatility,inTheMoney,contractSize,currency)')
    conn.commit()
    return conn, c
    
def calls_to_sql(conn, df):
    df = df.to_sql("calls", con=conn, if_exists='replace', index=False)
    return df

def calls(stock, next_exp_date):
    df = stock.option_chain(next_exp_date)
    df = df.calls
    return df

def create_puts_database():
    conn = sqlite3.connect('SPY.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS puts (contractSymbol,lastTradeDate,strike,lastPrice,bid,ask,change,percentChange,volume,openInterest,impliedVolatility,inTheMoney,contractSize,currency)')
    conn.commit()
    return conn, c
    
def puts_to_sql(conn, df):
    df = df.to_sql("puts", con=conn, if_exists='replace', index=False)
    return df

def puts(stock, next_exp_date):
    df = stock.option_chain(next_exp_date)
    df = df.puts
    return df

def step_one():
    stock = stock(url="SPY")
    exp_date = exp_dates(stock)
    df = calls(stock, exp_date)
    conn, c = create_calls_database()
    calls_to_sql(conn, df)
    return

def step_two():
    stock = stock(url="SPY")
    exp_date = exp_dates(stock)
    df = puts(stock, exp_date)
    conn, c = create_puts_database()
    puts_to_sql(conn, df)
    return

step_one()
step_two()
