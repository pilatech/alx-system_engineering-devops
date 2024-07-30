#!/usr/bin/python3
"""Module for getting todo employee data into JSON
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
        employee_JSON = '{"' + str(eid) + '": ['
        todos_s = len(user_todos)
        for i in range(todos_s):
            line = '{"task": "' + user_todos[i].get('title') + '", '
            completed = str(user_todos[i].get('completed')).lower()
            line += '"completed": ' + completed + ', '
            line += '"username": "' + employee.get('username')
            line += '"}'
            if i != todos_s - 1:
                line += ', '
            employee_JSON += line
        employee_JSON += ']}'

        with open(f"{eid}.json", 'w') as f:
            f.write(employee_JSON)
