import sys
import requests

def get_employee_todo_progress(employee_id):
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        done_tasks = [task for task in data if task['completed']]
        total_tasks = len(data)

        employee_name = data[0]['username'].capitalize()
        number_of_done_tasks = len(done_tasks)

        print(f'Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):')

        for task in done_tasks:
            print(f'\t{task["title"]}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 0-gather_data_from_an_API.py <employee_id>')
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
