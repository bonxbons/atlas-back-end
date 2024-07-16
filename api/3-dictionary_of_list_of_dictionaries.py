#!/usr/bin/python3

"""
Fetches and processes todos and users data from JSONPlaceholder API, 
and exports the result to a JSON file.
"""

import json
import requests


def get_tasks():
    """Fetches and processes todos and users data from JSONPlaceholder API."""
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    todos = response.json()

    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users = response.json()

    tasks = {}
    for user in users:
        user_id = user["id"]
        tasks[user_id] = []
        for todo in todos:
            if todo["userId"] == user_id:
                task = {
                    "username": user["username"],
                    "task": todo["title"],
                    "completed": todo["completed"]
                }
                tasks[user_id].append(task)

    return tasks


def export_to_json(tasks):
    """Exports tasks dictionary to a JSON file."""
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(tasks, json_file, indent=4)


if __name__ == "__main__":
    tasks = get_tasks()
    export_to_json(tasks)
