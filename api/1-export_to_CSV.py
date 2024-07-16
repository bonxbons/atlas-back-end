import csv
import requests
import sys

"""
Exports tasks of a given employee to a CSV file.

Usage: python3 1-export_to_CSV.py <employee_id>
"""

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    todos = response.json()

    employee_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    employee_response = requests.get(employee_url)
    employee = employee_response.json()

    employee_name = employee.get("name")

    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for todo in todos:
            if todo.get("userId") == employee_id:
                writer.writerow([
                    employee_id,
                    employee_name,
                    todo.get("completed"),
                    todo.get("title")
                ])
