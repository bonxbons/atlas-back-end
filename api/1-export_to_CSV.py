#!/usr/bin/python3

"""
Exports tasks of a given employee to a CSV file.

Usage: python3 1-export_to_CSV.py <employee_id>
"""

import csv
import requests
import sys

if __name__ == "__main__":
    # Check if the employee ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
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

    # Print the employee name for debugging
    print(f"Employee Name: {employee_name}")

    # Open the CSV file for writing
    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        # Write the header row
        header = [
            "USER_ID",
            "USERNAME",
            "TASK_COMPLETED_STATUS",
            "TASK_TITLE"
        ]
        writer.writerow(header)

        task_count = 0

        # Loop through the todos and write each task to the CSV file
        for todo in todos:
            if todo.get("userId") == employee_id:
                row = [
                    employee_id,
                    employee_name,
                    todo.get("completed"),
                    todo.get("title")
                ]
                writer.writerow(row)
                task_count += 1
                print(f"Task added: {todo.get('title')} (Completed: "
                      f"{todo.get('completed')})")

    # Print the number of tasks in the CSV file
    print(f"Number of tasks in CSV: {task_count}")
