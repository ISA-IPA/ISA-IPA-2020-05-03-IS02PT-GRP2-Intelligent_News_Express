from pyteaser import Summarize, SummarizeUrl
from pprint import pprint
import pandas as pd
import numpy as np
import tagui as t
import sqlite3
from sqlite3 import Error
from datetime import datetime
import util

def run():
	conn = util.create_connection("./db/news.db")
	site = util.getSiteByName(conn, "New York Times")
	site_url = site[0][2]
	site_id = site[0][0]

	t.init(visual_automation = True, chrome_browser = True)
	t.url(site_url)
	t.wait(10)
	df = catchContent()
	df = util.fixImgLink(df,"https://cf-templates-fghyux9ggb7t-ap-southeast-1.s3-ap-southeast-1.amazonaws.com/NewYorkTimes.png")
	df = util.fixSummary(df)
	t.wait(20)
	t.close()

	util.updateNews(conn, site_id, df)

def catchContent():
	number = t.count('(//li[contains(@class, "css-1iski2w")]/a)')
	df = pd.DataFrame(index=range(0,number), columns = ['Sno', 'Title', 'URL', 'Summary','Img_URL'])

	for n in range(1, number+1):
		title=t.read('//li[contains(@class, "css-1iski2w")][{}]/a/div'.format(n))
		URL=t.read('//li[contains(@class, "css-1iski2w")][{}]//@href'.format(n))
		Img_link=t.read('//li[contains(@class, "css-1iski2w")][{}]//img/@src'.format(n))
		summaries = SummarizeUrl(URL)

		df.iloc[n-1, 0] = n
		df.iloc[n-1, 1] = title.decode('utf-8')
		df.iloc[n-1, 2] = URL
		df.iloc[n-1, 3] = summaries
		df.iloc[n-1, 4] = Img_link

	df['Summary'].replace('None', np.nan, inplace=True)
	df.dropna(subset=['Summary'], inplace=True, how='any')
	df= df.reset_index(drop=True)
	df['Sno'] = df.index

	return df