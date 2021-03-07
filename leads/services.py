# import os
# import requests
# import json

# r = requests.get("https://jobs.github.com/positions.json?description=python&full_time=true&location=remote")
# json_object = json.loads(r.text)

# # print(r.status_code)
# print(json.dumps(json_object, indent = 1)) 



# for i in json_object:
#     print(i['id'])