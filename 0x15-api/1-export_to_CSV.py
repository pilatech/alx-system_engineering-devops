#!/usr/bin/python3
"""This script makes an API request and add data to CSV file"""

if __name__ == "__main__":
    import csv
    import json
    import requests
    import sys

    csv_file = f"{sys.argv[1]}.csv"
    user_id = sys.argv[1]
    todo_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    todo_req = requests.get(todo_url)
    todos = json.loads(todo_req.text)

    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user_req = requests.get(user_url)
    user = json.loads(user_req.text)

    total = len(todos)
    with open(csv_file, 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for i in todos:
            username = user.get('username')
            done = i.get('completed')
            title = i.get('title')
            writer.writerow([user_id, username, done, title])
