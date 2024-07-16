#!/usr/bin/python3

"""
Exports tasks of a given employee to a JSON file.

Usage: python3 2-export_to_JSON.py <employee_id>
"""

import json
import requests
import sys

if __name__ == "__main__":
    # Check if the employee ID is provided as a command-line argument
    if len(sys.argv)!= 2:
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
