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
	site = util.getSiteByName(conn, "Today Online")
	site_url = site[0][2]
	site_id = site[0][0]

	t.init(visual_automation = True, chrome_browser = True)
	t.url(site_url)
	t.wait(2)
	t.hover('//div[@class="container footer-main"]')
	t.wait(6)
	df = catchContent()
	t.wait(20)
	t.close()

	util.updateNews(conn, site_id, df)

def catchContent():
	number_to = t.count('(//div[@class="col"]/div[contains(@class, "today")]/ul/li[contains(@class, "col-md-12")])')

	df_to = pd.DataFrame(index=range(0,number_to), columns = ['Sno', 'Title', 'URL', 'Summary','Img_URL'])

	t.hover('//div[@class="container footer-main"]')
	t.wait(2)

	for n in range(1, number_to):
		title=t.read('//div[@class="col"]/div[contains(@class, "today")]/ul/li[contains(@class, "col-md-12")][{}]//div[contains(@class, "article-listing_content")]//h2'.format(n))
		URL_o=t.read('//div[@class="col"]/div[contains(@class, "today")]/ul/li[contains(@class, "col-md-12")][{}]//@href'.format(n))
		URL = "https://www.todayonline.com" + str(URL_o) 

		Img_link=t.read('//div[@class="col"]/div[contains(@class, "today")]/ul/li[contains(@class, "col-md-12")][{}]//img/@src'.format(n))

		df_to.iloc[n-1, 0] = n
		df_to.iloc[n-1, 1] = title.decode('utf-8')
		df_to.iloc[n-1, 2] = URL
		df_to.iloc[n-1, 4] = Img_link

	for i in range(0, df_to.shape[0]):
		if df_to['Img_URL'][i]=="":
			df_to['Img_URL'][i]=np.nan

	df_to.dropna(subset=['Img_URL'], inplace=True, how='any')
	df_to= df_to.reset_index(drop=True)
	df_to['Sno'] = df_to.index

	df_to = util.fixImgLink(df_to, "https://cf-templates-fghyux9ggb7t-ap-southeast-1.s3-ap-southeast-1.amazonaws.com/todayOnline.png")

	for n in range(0, df_to.shape[0]):   
		t.url(df_to.URL[n])
		t.wait(4)
		t.hover('//div[@class="article-detail_subscription"]')
		t.wait(2)

		number_p = t.count('//div/p[not(@class)]')

		Content = ""

		for i in range(1, number_p-2):
		    cont=t.read('//div/p[not(@class)][{}]'.format(i))
		    Content = Content + "" + cont
 
		summaries = Summarize(df_to.Title[n], unicode(str(Content), "utf-8"))
		df_to.iloc[n-1, 3] = summaries[0]

	return df_to