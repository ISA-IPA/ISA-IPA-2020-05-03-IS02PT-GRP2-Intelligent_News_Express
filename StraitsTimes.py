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
	site = util.getSiteByName(conn, "StraitsTimes")
	site_url = site[0][2]
	site_id = site[0][0]

	t.init(visual_automation = True, chrome_browser = True)
	t.url(site_url)
	t.wait(10)
	df = catchContent()
	df = util.fixSummary(df)
	t.wait(60)
	t.close()

	util.updateNews(conn, site_id, df)

def catchContent():
	number_bb = t.count('(//div[contains(@data-vr-zone, "Top Stories")]//span[contains(@class, "story-headline")])')

	df_bb = pd.DataFrame(index=range(0,number_bb-2), columns = ['Sno', 'Title', 'URL', 'Summary','Img_URL'])

	for n in range(0, number_bb-2):
		title=t.read('//div[contains(@data-vr-zone, "Top Stories {}")]//span[contains(@class, "story-headline")]'.format(n))
		URL_b=t.read('//div[contains(@data-vr-zone, "Top Stories {}")]//span[contains(@class, "story-headline")]//@href'.format(n))
		URL = "https://www.straitstimes.com/" + str(URL_b)
		Img_URL = t.read('//div[contains(@data-vr-zone, "Top Stories {}")]//span[contains(@class, "story-headline")]/ancestor::div[contains(@class, "body")]/..//img/@src'.format(n))
		summaries = SummarizeUrl(URL)
		df_bb.iloc[n, 0] = n
		df_bb.iloc[n, 1] = title
		df_bb.iloc[n, 2] = URL
		df_bb.iloc[n, 3] = summaries
		df_bb.iloc[n, 4] = Img_URL

	return df_bb