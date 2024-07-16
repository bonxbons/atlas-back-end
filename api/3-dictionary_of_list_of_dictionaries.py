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
