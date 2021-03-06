import csv
import os
import requests


token = os.environ.get('TOKEN')

# read all story ID
with open('Clubhouse Backlog - clubhouseBacklog.csv') as story_file:
    csv_reader = csv.reader(story_file, delimiter=',')
    story_ids = [x[1] for x in csv_reader][1:]


# get stories from clubhose and convert to csv
with open('clubhouse conversion.csv', mode='w') as csv_file:
    fieldnames = [
        'entity_type',
        'archived',
        'created_at',
        'updated_at',
        'id',
        'external_id',
        'name',
        'story_type',
        'position',
        'workflow_state_id',
        'moved_at',
        'started',
        'started_at',
        'started_at_override',
        'completed',
        'completed_at',
        'completed_at_override',
        'blocker',
        'blocked',
        'estimate',
        'deadline',
        'project_id',
        'labels',
        'requested_by_id',
        'owner_ids',
        'follower_ids',
        'mention_ids',
        'epic_id',
        'story_links',
        'app_url',
        'description',
        'branches',
        'comments',
        'commits',
        'files',
        'linked_files',
        'tasks'
    ]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    for (count, _id) in enumerate(story_ids):
        url = f'https://api.clubhouse.io/api/v2/stories/{_id}?token={token}'
        resp = requests.get(url)
        if resp.status_code == 404:
            message = resp.json().get('message')
            writer.writerow({
                'entity_type': message
            })
            print(message)
        else:
            writer.writerow(resp.json())
        print(f'Story {count} successfully added')
