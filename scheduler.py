import datetime
import time
from apscheduler.scheduler import Scheduler

from pyteaser import Summarize, SummarizeUrl
from pprint import pprint
import pandas as pd
import numpy as np

import tagui as t
import logging

# Start the scheduler
sched = Scheduler()
sched.daemonic = False
sched.start()
logging.basicConfig()

def job_function():
	print("init tagui")

	t.init(visual_automation = True, chrome_browser = True)
	t.url('https://www.nytimes.com/trending/')
	number = t.count('(//li[contains(@class, "css-1iski2w")]/a)')

	df = pd.DataFrame(index=range(0,number), columns = ['Sno', 'Title', 'URL', 'Summary'])

	for n in range(1, number+1):
		title=t.read('//li[contains(@class, "css-1iski2w")][{}]/a/div'.format(n))
		URL=t.read('//li[contains(@class, "css-1iski2w")][{}]//@href'.format(n))
		summaries = SummarizeUrl(URL)
	    
		df.iloc[n-1, 0] = n
		df.iloc[n-1, 1] = title
		df.iloc[n-1, 2] = URL
		df.iloc[n-1, 3] = summaries
	
	t.close()
	print("Data loaded, closing chrome")	
	#print("Title: "+str(df.iloc[3, 1])+"\n")
	#print("Summary: "+str(df.iloc[3, 3]))
	now = datetime.datetime.now()
	date_time = now.strftime("%m/%d/%Y/%H%M%S")	
	df.to_csv("NYT_summary.csv")   
	print("csv file created")

# Schedules job_function to be run once each minute
sched.add_cron_job(job_function,  minute='0-59')