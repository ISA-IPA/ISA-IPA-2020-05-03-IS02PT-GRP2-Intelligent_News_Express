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
    cur.execute("SELECT * FROM news where latest=1")
    data = cur.fetchall()
    conn.close()
    resultList = buildNewsList(data)

    return resultList

def getNewsBySiteName(site_name):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("select * from news where latest=1 and site_id in (select id from site where name =?)",(site_name,))
    data = cur.fetchall()
    conn.close()
    resultList = buildNewsList(data)

    return resultList

def buildNewsList(data):
    tableList =[]
    for row in data:
        news = {"news_id": row[0],"site_id":row[1], "create_date":row[2], "title":row[3], "url":row[4], "summary": row[5],"img_url":row[6]}
        tableList.append(news)
    return tableList
