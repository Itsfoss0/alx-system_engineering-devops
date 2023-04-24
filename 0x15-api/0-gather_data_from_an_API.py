#!/usr/bin/python3

"""
A simple module to make API Calls
To a mockup API server and return the
Responses. Then print them out to standard output

Usage: ./0-gather-data_from_an_API <ID>
"""

from requests import get
from sys import argv

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "Thing Gecko/20100101 Firefox/102.0"
}
base_url = "https://jsonplaceholder.typicode.com/users/"


def get_task_status(user_id: str) -> None:
    """
    Get the task status for a certain user
    Args:
        user_id (str): The user id of the user
    """
    # lets first get the name of Employee
    emp_name = get(f"{base_url}{user_id}").json().get("name")
    total_tasks = 0
    full_url = "{}{}/todos/".format(base_url, user_id)
    response = get(full_url, headers=headers).json()
    # lets get the total number of tasks shall we?
    for _ in response[0].get('title'):
        total_tasks += 1

    # How about done tasks
    done_tasks = [task['title'] for task in response
                  if task['completed']]
    done_tasks_count = len(done_tasks)
    print("Employee {} is done with ({}/{}):".format(
        emp_name, done_tasks_count, total_tasks))
    [print("\t {}".format(task)) for task in done_tasks]


if __name__ == "__main__":
    get_task_status(argv[1])
