 #!/usr/bin/python3

import csv
import requests
import sys
import os

def get_employee_todo_progress(employee_id):
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    user_response = requests.get(user_url)

    if user_response.status_code != 200:
        print(f'Error: Unable to fetch user data for employee ID {employee_id}')
        return

    user_data = user_response.json()
    user_name = user_data['name']

    todos_url = (f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    todos_response = requests.get(todos_url)

    if todos_response.status_code != 200:
        print(f'Error: Unable to fetch todo data for employee ID {employee_id}')
        return

    tasks = todos_response.json()
    csv_file = open(f'{employee_id}.csv', 'w', newline='')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

    for task in tasks:
        csv_writer.writerow([employee_id, user_name, task['completed'], task['title']])

    csv_file.close()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 1-export_to_CSV.py <employee_id>')
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
