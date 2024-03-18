#!/usr/bin/python3
"""
Export data in the JSON format.

Requirements:
Records all tasks from all employees
Format must be: {
    "USER_ID": [
        {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
        {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
        ...
    ],
    "USER_ID": [
        {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
        {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
        ...
    ]
}
File name must be: todo_all_employees.json
"""

import json
import requests
from sys import argv


def export_to_json():
    """
    Export data to JSON file.
    """
    url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(url).json()
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todos = requests.get(todos_url).json()

    user_tasks = {}

    for user in users:
        user_id = user['id']
        username = user['username']
        user_tasks[user_id] = []
        for todo in todos:
            if todo['userId'] == user_id:
                task = {
                    "username": username,
                    "task": todo['title'],
                    "completed": todo['completed']
                }
                user_tasks[user_id].append(task)

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(user_tasks, json_file)


if __name__ == "__main__":
    export_to_json()
