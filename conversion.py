import csv
import os
import requests


token = os.getenv('token')

# read all story ID
with open('Clubhouse Backlog - clubhouseBacklog.csv') as story_file:
    csv_reader = csv.reader(story_file, delimiter=',')
    story_ids = [x[1] for x in csv_reader][1:]


for _id in story_ids:
    url = f'https://api.clubhouse.io/api/v2/stories/{_id}?token={token}'
    resp = requests.get(url)
    import pdb; pdb.set_trace()
    pass



