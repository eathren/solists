from datetime import datetime
import os

from apscheduler.schedulers.background import BackgroundScheduler
from fetchLeads import fetch_github_api

        
def start():
        scheduler = BackgroundScheduler()
        scheduler.add_job(fetch_github_api.save_new_jobs, 'interval', hours=6)
        scheduler.start()