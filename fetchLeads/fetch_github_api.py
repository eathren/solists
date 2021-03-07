import os
import requests
import json
from leads.models import Lead
import re
from datetime import datetime
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

def get_jobs_json():
    r = requests.get("https://jobs.github.com/positions.json?&description=&location=remote")
    json_object = json.loads(r.text)
    try:
        r.raise_for_status()
        return json.loads(r.text)
    except:
        return None
    
def save_new_jobs():
    print("hello 2")
    json_data = get_jobs_json()
    now = datetime.utcnow()
    today_data = True
    if json_data is not None:
        while today_data == True:
            for job in json_data:
                try: 
                    date_difference = now -  datetime.strptime(job["created_at"],  "%a %b %d %H:%M:%S %Z %Y")
                    print("Days", date_difference.days)
                    if date_difference.days == 0:
                        
                        new_job = Lead()
                        new_job.author = "Github Jobs"
                        new_job.developer = True
                        new_job.description = job["description"]
                        new_job.how_to_apply = job["how_to_apply"]
                        new_job.author = "Github Jobs"
                        if job["type"] == "Full Time":
                            new_job.job_type = 'Full-Time'
                        elif job["type"] == "Contract":
                            new_job.job_type = 'Contract'
                        new_job.title = job["title"]
                        new_job.company = job["company"]
                        application_url =  re.search(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", job["how_to_apply"] )
                        new_job.application_link = application_url[0]
                        new_job.user_author =  get_user_model().objects.get(pk='f3ee3abe-a186-44da-9ed2-b18ec3b570b7')
                        new_job.remote = 'Remote'
                        new_job.role = 'Developer'
                        new_job.save()
                        print('SUCCESS', new_job.title)
                    else:
                        print("No new data")
                        today_data = False
                        return today_data
                    
                except:
                    print("FAILED")
                    pass