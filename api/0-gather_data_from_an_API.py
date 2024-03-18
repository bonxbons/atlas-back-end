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

    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    todos_response = requests.get(todos_url)

    if todos_response.status_code != 200:
        print(f'Error: Unable to fetch todo data for employee ID {employee_id}')
        return

    total_tasks = len(todos_response.json())
    completed_tasks = sum(task['completed'] for task in todos_response.json())

    print(f'Employee {user_name} is done with tasks({completed_tasks}/{total_tasks}):')

    completed_tasks_titles = [task['title'] for task in todos_response.json() if task['completed']]

    for task_title in completed_tasks_titles:
        print(f'\t{task_title}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 0-gather_data_from_an_API.py <employee_id>')
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
