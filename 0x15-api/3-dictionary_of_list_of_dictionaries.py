#!/usr/bin/python3
"""Module for getting todo employee data into JSON
It takes employee ID as an argument and works out their todos
"""

import json
import requests

if __name__ == "__main__":
    r = requests.get("https://jsonplaceholder.typicode.com/users")
    employee_JSON = '{'
    employees = r.json()
    emp_s = len(employees)
    for k in range(emp_s):
        cid = employees[k].get('id')
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
        employee_JSON += '"' + str(eid) + '": ['
        todos_s = len(user_todos)
        for i in range(todos_s):
            line = '{"username": "' + employee.get('username') + '", '
            line += '"task": "' + user_todos[i].get('title') + '", '
            completed = str(user_todos[i].get('completed')).lower()
            line += '"completed": ' + completed
            line += '}'
            if i != todos_s - 1:
                line += ', '
            employee_JSON += line
        employee_JSON += ']'
        if k < emp_s - 1:
            employee_JSON += ', '
    employee_JSON += '}'

    with open(f"todo_all_employees.json", 'w') as f:
        f.write(employee_JSON)
