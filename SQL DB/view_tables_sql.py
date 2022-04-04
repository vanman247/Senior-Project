import sqlite3
import pandas as pd

def access_db():
    con = sqlite3.connect("SPY.db")
    c = con.cursor()
    return con, c

def view_tables(con, c):
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(c.fetchall())


def access_table(con, c, tab):
    df = pd.read_sql('SELECT * FROM calls_2022_03_08_exp_2022_03_09', con)
    print(df.head(20))
    return df


con, c = access_db()
view_tables(con, c)
access_table(con, c)
