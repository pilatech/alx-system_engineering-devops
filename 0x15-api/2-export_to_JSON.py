#!/usr/bin/python3
"""This script makes an API request and saves to JSON file"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    user_id = sys.argv[1]
    todo_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    todo_req = requests.get(todo_url)
    todos = json.loads(todo_req.text)

    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user_req = requests.get(user_url)
    user = json.loads(user_req.text)

    unm = user.get('username')
    uid = user.get('id')
    json_file = f"{uid}.json"
    tasks = {}
    tasks[uid] = []
    for i in todos:
        done = i.get('completed')
        task = i.get('title')
        tasks[uid].append({"task": task, "completed": done, "username": unm})

    with open(json_file, 'w') as file:
        json.dump(tasks, file)
