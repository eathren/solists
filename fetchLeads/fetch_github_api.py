import os
import requests
import json
from leads.models import Lead
import re
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
#from scheduler.config_stuff import config

def get_jobs_json():
    r = requests.get("https://jobs.github.com/positions.json?&description=&location=remote")
    json_object = json.loads(r.text)
    # print("hello3")
    # print(json_object)
    try:
        r.raise_for_status()
        # print("hello5")
        return json.loads(r.text)
    except:
        return None
    
def save_new_jobs():
    print("hello 2")
    json_data = get_jobs_json()
    if json_data is not None:
        # print("Hello 6")
        for job in json_data:
            
            # print("hello 7")
            try: 
                # print("Hello4")
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
                # if 'REMOTE' in  job["location"].upper():
                #     new_job.remote = "Remote"
                new_job.title = job["title"]
                new_job.company = job["company"]
                application_url =  re.search(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", job["how_to_apply"] )
                new_job.application_link = application_url[0]
                new_job.user_author =  get_user_model().objects.get(pk='f3ee3abe-a186-44da-9ed2-b18ec3b570b7')
                # print("T13", new_job.user_author)
                # print("NEW JOB", new_job)
                new_job.remote = 'Remote'
                new_job.role = 'Developer'
                # print("T14")
                # print("Test",new_job.save())
                new_job.save()
                print("SUCCESS", new_job.title)
                # print("T15")
                
            except:
                print("FAILED")
                pass
# print("hello 1")