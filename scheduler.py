import datetime
import time
from apscheduler.scheduler import Scheduler

from pyteaser import Summarize, SummarizeUrl
from pprint import pprint
import pandas as pd
import numpy as np

import tagui as t
import logging
import StraitsTimes, bbc, NewYorkTimes, todayOnline, wordCloud

# Start the scheduler
sched = Scheduler()
sched.daemonic = False
sched.start()
logging.basicConfig()

def job_function():
	print("Job Start")
	print("StraitsTimes Start")
	StraitsTimes.run()
	print("StraitsTimes End")
	print("NewYorkTimes Start")
	NewYorkTimes.run()
	print("NewYorkTimes End")
	print("todayOnline Start")
	todayOnline.run()
	print("todayOnline End")
	print("BBC Start")
	bbc.run()
	print("BBC End")
	print("wordCloud Start")
	wordCloud.run()
	print("wordCloud End")
	print("Job End")

# Schedules job_function to be run once each hour
sched.add_cron_job(job_function,  hour='0-23')
