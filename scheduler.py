import datetime
import time
from apscheduler.scheduler import Scheduler

from pyteaser import Summarize, SummarizeUrl
from pprint import pprint
import pandas as pd
import numpy as np

import tagui as t
import logging
import StraitsTimes, bbc, NewYorkTimes, wordCloud

# Start the scheduler
sched = Scheduler()
sched.daemonic = False
sched.start()
logging.basicConfig()

def job_function():
	print("Job Start")
	wordCloud.run()
	print("Job End")

# Schedules job_function to be run once each hour
sched.add_cron_job(job_function,  minute='0-60')
