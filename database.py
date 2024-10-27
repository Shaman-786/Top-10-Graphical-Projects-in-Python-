import json

def init_db():
    # Load users and lessons from JSON files
    with open('data/users.json') as f:
        users = json.load(f)
    with open('data/lessons.json') as f:
        lessons = json.load(f)
    return users, lessons
