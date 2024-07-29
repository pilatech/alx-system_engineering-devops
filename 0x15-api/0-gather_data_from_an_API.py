#!/usr/bin/python3
"""Module for importing and displaying employee data"""


import json
import requests
import sys

if len(sys.argv) >= 2:
    cid = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{cid}"
    r = requests.get(user_url)
    employee = r.json()
    eid = employee.get('id')
    name = employee.get('name')
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    r = requests.get(todos_url)
    all_todos = r.json()
    user_todos = []
    done = []
    for todo in all_todos:
        if todo.get('userId') == int(cid):
            user_todos.append(todo)
    for todo in user_todos:
        if todo.get('completed'):
            done.append(todo)
    done_s = len(done)
    user_s = len(user_todos)
    print(f"Employee {name} is done with tasks({done_s}/{user_s}):")
    for todo in done:
        print(f"\t {todo.get('title')}")
