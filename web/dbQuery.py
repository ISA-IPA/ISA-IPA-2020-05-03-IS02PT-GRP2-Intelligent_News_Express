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
    tableList = buildNewsTable(data)
    columns = [
        {
            "field": "news_id", # which is the field's name of data key 
            "title": "News ID", # display as the table header's name
            "sortable": True,
        },
        {
            "field": "site_id",
            "title": "Site ID",
            "sortable": True,
        },
        {
            "field": "create_date",
            "title": "Create Date",
            "sortable": True,
        },
        {
            "field": "title",
            "title": "Title",
            "sortable": True,
        },
        {
            "field": "url",
            "title": "URL",
            "sortable": True,
        },
        {
            "field": "summary",
            "title": "Summary",
            "sortable": True,
        }
    ]

    return tableList,columns


def buildNewsTable(data):
    tableList =[]
    for row in data:
        news = {"news_id": row[0],"site_id":row[1], "create_date":row[2], "title":row[3], "url":row[4], "summary": row[5]}
        tableList.append(news)
    return tableList
