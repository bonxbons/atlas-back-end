#!/usr/bin/python3
"""
Script that, using a REST API, for a given employee ID, returns information
about his/her TODO list progress.
"""
import requests
from sys import argv

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(argv) != 2:
        print("Usage: {} employee_id".format(argv[0]))
        exit(1)

    # Base URL for the API
    base_url = 'https://jsonplaceholder.typicode.com/'

    # Employee ID provided as command-line argument
    employee_id = argv[1]

    # Fetch user info
    user_response = requests.get(base_url + 'users/{}'.format(employee_id))
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch todos for the user
    todos_response = requests.get(base_url + 'todos?userId={}'.format(employee_id))
    todos_data = todos_response.json()

    # Count total and completed tasks
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo.get('completed'))

    # Print employee information
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, completed_tasks, total_tasks))

    # Print titles of completed tasks
    for todo in todos_data:
        if todo.get('completed'):
            print("\t {}".format(todo.get('title')))

