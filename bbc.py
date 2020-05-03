from pyteaser import Summarize, SummarizeUrl
from pprint import pprint
import pandas as pd
import numpy as np
import sqlite3
from sqlite3 import Error
from datetime import datetime
import requests
import util

def run():
	conn = util.create_connection("./db/news.db")
	site = util.getSiteByName(conn, "BBC News")
	site_url = site[0][2]
	site_id = site[0][0]

	results, url, number_BBC, Img_link = NewsFromBBC(site_url)
	df = pd.DataFrame(index=range(0,number_BBC-1), columns = ['Sno', 'Title', 'URL','Summary', 'Img_URL'])
	
	for i in range(1, number_BBC):
		summaries = SummarizeUrl(url[i])

		df.iloc[i-1, 0] = i
		df.iloc[i-1, 1] = results[i]
		df.iloc[i-1, 2] = url[i]
		df.iloc[i-1, 3] = summaries
		df.iloc[i-1, 4] = Img_link[i]

	df = util.fixImgLink(df, "https://cf-templates-fghyux9ggb7t-ap-southeast-1.s3-ap-southeast-1.amazonaws.com/bbc.png")
	df = util.fixSummary(df)

	util.updateNews(conn, site_id, df)

# BBC top news
def NewsFromBBC(site_url):    
	# BBC news api
	main_url = site_url
 
	# fetching data in json format
	open_bbc_page = requests.get(main_url).json()
 
	# getting all articles in a string article
	article = open_bbc_page["articles"]
 
	# empty list which will 
	# contain all trending news
	results = []
	url = []
	Img_link = []
	 
	for ar in article:
		results.append(ar["title"])
		url.append(ar["url"])
		Img_link.append(ar["urlToImage"])
		 
		number_BBC = len(results)
	
	return results, url, number_BBC, Img_link