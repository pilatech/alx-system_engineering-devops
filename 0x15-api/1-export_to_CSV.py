#!/usr/bin/python3
"""Module for getting todo employee data into .csv
It takes employee ID as an argument and works out their todos
"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        cid = sys.argv[1]
        user_url = f"https://jsonplaceholder.typicode.com/users/{cid}"
        r = requests.get(user_url)
        employee = r.json()
        eid = employee.get('id')
        todos_url = "https://jsonplaceholder.typicode.com/todos"
        r = requests.get(todos_url)
        all_todos = r.json()
        user_todos = []
        done = []
        for todo in all_todos:
            if todo.get('userId') == int(cid):
                user_todos.append(todo)
        employee_csv = ''
        for todo in user_todos:
            line = '"' + str(eid)
            line += '","' + employee.get('username')
            line += '","' + str(todo.get('completed'))
            line += '","' + todo.get('title') + '"\n'
            employee_csv += line

        with open(f"{eid}.csv", 'w') as f:
            f.write(employee_csv)
