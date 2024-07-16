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
