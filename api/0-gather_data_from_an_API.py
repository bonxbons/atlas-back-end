#!/usr/bin/python3

"""
This script gathers data from an API and prints the results.
"""

import requests
import sys

if __name__ == "__main__":
    # Check if the script is called with the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    # Get the employee ID from the command line argument
    employee_id = int(sys.argv[1])

    # Get the list of todos from the API
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    todos = response.json()

    # Get the employee data from the API
    employee_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    employee_response = requests.get(employee_url)
    employee = employee_response.json()

    # Extract the employee name
    employee_name = employee.get("name")

    # Filter completed tasks for the employee
    completed_tasks = [todo.get("title") for todo in todos if todo.get("userId") == employee_id and todo.get("completed")]

    # Count the total number of tasks for the employee
    total_tasks = len([todo for todo in todos if todo.get("userId") == employee_id])

    # Print the employee's name and task completion status
    print("Employee {} is done with tasks({}/{}):".format(employee_name, len(completed_tasks), total_tasks))

    # Print each completed task
    for task in completed_tasks:
        print("\t{}".format(task))
