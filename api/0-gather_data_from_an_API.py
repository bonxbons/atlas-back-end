#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    user_response = requests.get(user_url)

    if user_response.status_code != 200:
        print(f'Error: Unable to fetch user data for employee ID {employee_id}')
        return

    user_data = user_response.json()
    user_name = user_data['name']

    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    todos_response = requests.get(todos_url)

    if todos_response.status_code != 200:
        print(f'Error: Unable to fetch todo data for employee ID {employee_id}')
        return

    total_tasks = 0
    completed_tasks = 0

    for task in todos_response.json():
        if task['userId'] == employee_id:
            total_tasks += 1
            if task['completed']:
                completed_tasks += 1

    print(f'Employee {user_name} is done with tasks({completed_tasks}/{total_tasks}):')

    done_tasks = [task['title'] for task in todos_response.json()
                  if task['userId'] == employee_id and task['completed']]

    for task_title in done_tasks:
        print(f'\t{task_title}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 0-gather_data_from_an_API.py <employee_id>')
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo
