#!/usr/bin/python3
"""script that fetches info about a given employee's ID using an api"""
import json
import requests
import sys

base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":

    user_id = sys.argv[1]

    # Get user info e.g https://jsonplaceholder.typicode.com/users/1/
    user_url = '{}/users?id={}'.format(base_url, user_id)

    # Get info from API
    response = requests.get(user_url)
    # Parse the data into JSON format
    data = json.loads(response.text)
    # Extract user data, in this case, name of employee
    username = data[0].get('name')

    # Get user info about todo tasks
    tasks_url = '{}/todos?userId={}'.format(base_url, user_id)

    # Get info from API
    response = requests.get(tasks_url)
    # Parse the data into JSON format
    tasks = json.loads(response.text)

    # Initialize list to store task records
    task_records = []

    # Loop through tasks and record task data
    for task in tasks:
        task_record = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        }
        task_records.append(task_record)

    # Create JSON data
    json_data = {user_id: task_records}

    # Write data to JSON file
    json_file_name = "{}.json".format(user_id)
    with open(json_file_name, 'w') as json_file:
        json.dump(json_data, json_file)

    print("Data exported to", json_file_name)
