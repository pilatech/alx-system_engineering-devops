#!/usr/bin/python3
"""This script makes an API request and display data"""

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

    completed = []
    total = len(todos)
    for i in todos:
        if (i.get('completed')):
            completed.append(i.get('title'))

    done = len(completed)
    print(f"Employee {user.get('name')} is done with tasks({done}/{total}):")
    for todo in completed:
        print(f"    {todo}")
