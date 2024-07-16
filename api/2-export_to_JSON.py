#!/usr/bin/python3

"""
Exports tasks of a given employee to a JSON file.
"""

import json
import requests
import sys

if __name__ == "__main__":
    # Check if the employee ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    # Get the employee ID from the command-line argument
    employee_id = int(sys.argv[1])

    # Fetch the todos data from the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    todos = response.json()

    # Fetch the employee data from the JSONPlaceholder API
    employee_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)
    employee_response = requests.get(employee_url)
    employee = employee_response.json()

    # Get the employee name
    employee_name = employee.get("name")

    # Create a dictionary to store the tasks
    tasks = {str(employee_id): []}

    # Loop through the todos and add each task to the dictionary
    for todo in todos:
        if todo.get("userId") == employee_id:
            task = {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": employee_name
            }
            tasks[str(employee_id)].append(task)

    # Open the JSON file for writing
    with open("{}.json".format(employee_id), "w") as json_file:
        json.dump(tasks, json_file, indent=4)

    print("JSON file created successfully!")
