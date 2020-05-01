import sqlite3
import pandas as pd

pd.set_option('display.max_colwidth', -1)

def create_connection():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect("../db/news.db")
        print("DB Connection setup")
    except Error as e:
        print(e)
    finally:
        if conn:
            return conn
        else:
            print("DB Connection failed")

def getSiteByName(name):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM site where name=?",(name,))
    rows = cur.fetchall()
    conn.close()
    return rows

def getAllNews():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM news")
    data = cur.fetchall()
    conn.close()

    columnNames = ("News ID","Site ID","Create Date", "Title","URL","Summary")
    df = pd.DataFrame(data, columns=columnNames)

    return df

