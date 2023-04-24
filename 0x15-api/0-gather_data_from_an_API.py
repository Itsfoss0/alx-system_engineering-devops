#!/usr/bin/python3

'''
A simple module to make API Calls
To a mockup API server and return the
resps. Then print them out to standard output
Usage: ./0-gather-data_from_an_API <ID>
Where <ID> is the employee ID for whom we want to list
The tasks
'''

import requests
import sys

API_BASE_URL = "https://jsonplaceholder.typicode.com"
API_USER_URL = f"{API_BASE_URL}/users"
API_TASK_URL = f"{API_BASE_URL}/todos"

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "Thing Gecko/20100101 Firefox/102.0"
}


def get_employee_name(user_id: str) -> str:
    """
    Get the name of an employee
    Args:
        user_id (str): The user id of the employee
    Returns:
        str: The name of the employee
    """
    resp = requests.get(f"{API_USER_URL}/{user_id}", headers=HEADERS)
    if resp.status_code != 200:
        raise ValueError(f"Invalid resp status code: {resp.status_code}")
    return resp.json().get("name")


def get_tasks(user_id: str) -> list:
    """
    Get the tasks of an employee
    Args:
        user_id (str): The user id of the employee
    Returns:
        list: The list of tasks of the employee
    """
    resp = requests.get(f"{API_TASK_URL}?userId={user_id}", headers=HEADERS)
    if resp.status_code != 200:
        raise ValueError(f"Invalid resp status code: {resp.status_code}")
    return resp.json()


def print_task_status(user_id: str) -> None:
    """
    Print the status of an employee's tasks
    Args:
        user_id (str): The user id of the employee
    """
    employee_name = get_employee_name(user_id)
    tasks = get_tasks(user_id)

    total_tasks = len(tasks)
    done_tasks = [task for task in tasks if task['completed']]
    done_tasks_count = len(done_tasks)

    print(f"Employee {employee_name} is done with\
    ({done_tasks_count}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <ID>")
        sys.exit(1)
    try:
        print_task_status(sys.argv[1])
    except ValueError as e:
        print(e)
        sys.exit(1)
