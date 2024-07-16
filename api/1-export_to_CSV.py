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
    if len(sys.argv)!= 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    # Get the employee ID from the command-line argument
    employee_id = int(sys.argv[1])

    # Fetch the todos data from the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    todos = response.json()

    # Fetch the employee data from the JSONPlaceholder API
    employee_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    employee_response = requests.get(employee_url)
    employee = employee_response.json()

    # Get the employee name
    employee_name = employee.get("name")

    # Open the CSV file for writing
    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        # Write the header row
        writer.writerow((
            "USER_ID",  # USER_ID
            "USERNAME",  # USERNAME
            "TASK_COMPLETED_STATUS",  # TASK_COMPLETED_STATUS
            "TASK_TITLE"  # TASK_TITLE
        ))

        task_count = 0  # Initialize task count

        # Loop through the todos and write each task to the CSV file
        for todo in todos:
            if todo.get("userId") == employee_id:
                writer.writerow((
                    employee_id,  # USER_ID
                    employee_name,  # USERNAME
                    todo.get("completed"),  # TASK_COMPLETED_STATUS
                    todo.get("title")  # TASK_TITLE
                ))
                task_count += 1  # Increment task count

    # Print the number of tasks in the CSV file
    with open("{}.csv".format(employee_id), "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        task_count = sum(1 for row in reader)
        
