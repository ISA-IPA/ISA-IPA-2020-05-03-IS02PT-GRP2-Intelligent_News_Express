import sqlite3
from sqlite3 import Error
import pandas as pd
from datetime import datetime

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("DB Connection setup")
    except Error as e:
        print(e)
    finally:
        if conn:
            return conn
        else:
            print("DB Connection failed")

def getSiteByName(conn, name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM site where name=?",(name,))
    rows = cur.fetchall()
    return rows

def insertNews(conn,news):    
    sql = ''' INSERT INTO news(site_id,create_date,title,url,summary,img_url,latest)
              VALUES(?,?,?,?,?,?,1) '''
    cur = conn.cursor()
    cur.execute(sql, news)
    return cur.lastrowid

def markNews(conn, site_id):
    cur = conn.cursor()
    cur.execute("UPDATE news set latest=0 where latest=1 and site_id=? ",(site_id,))

def updateNews(conn, site_id, df):
    now = datetime.now()
    # dd/mm/YY
    dt_string = now.strftime("%d/%m/%Y")
    markNews(conn, site_id)
    for index, row in df.iterrows():
        title = row['Title']
        url = row['URL']
        summary = row['Summary']
        img_url = row['Img_URL']
        news = (site_id,dt_string,title,url,summary,img_url)
        news_id = insertNews(conn,news)
    print("News %d has been created" % news_id)   
    conn.commit()
    conn.close()
    print("DB connection Closed")

def getAllSummary(conn):
    cur = conn.cursor()
    cur.execute("SELECT summary FROM news where latest=1")
    rows = cur.fetchall()
    conn.close()
    return rows

def remove_str(summm_l, SS):
    summm = ''.join(summm_l)
    summm = summm.encode('utf-8').decode('utf-8', 'ignore')
    if SS in summm:
        summm = summm.replace(SS, '')
    
    return summm

def fixSummary(df):
    for i in range(0, df.shape[0]):
        df['Summary'][i] = remove_str(df['Summary'][i], "u'")
    return df