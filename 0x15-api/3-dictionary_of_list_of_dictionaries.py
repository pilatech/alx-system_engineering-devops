#!/usr/bin/python3
"""This script makes an API request and saves to JSON file"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    todo_url = f"https://jsonplaceholder.typicode.com/todos"
    todo_req = requests.get(todo_url)
    todos = json.loads(todo_req.text)

    tasks = {}
    total = len(todos)
    for i in todos:
        UID = i.get('userId')
        tl = i.get('title')
        done = i.get('completed')
        user_url = f"https://jsonplaceholder.typicode.com/users/{UID}"
        user_req = requests.get(user_url)
        user = json.loads(user_req.text)

        us = user.get('username')

        if (UID in tasks):
            tasks[UID].append({'username': us, "task": tl, "completed": done})
        else:
            tasks[UID] = []
            tasks[UID].append({'username': us, "task": tl, "completed": done})

    with open("todo_all_employees.json", "w") as file:
        json.dump(tasks, file)
