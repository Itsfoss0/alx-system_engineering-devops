#!/usr/bin/python3
"""A simple module to make API Calls
To a mockup API server and return the
Responses. Then print them out to standard output
Usage: ./0-gather-data_from_an_API <ID>
Where <ID> is the employee ID for whom we want to list
The tasks"""

from json import dump
from requests import get
from sys import argv

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "Thing Gecko/20100101 Firefox/102.0"
}
base_url = "https://jsonplaceholder.typicode.com/users/"


def save_tasks_to_json(user_id: str) -> None:
    """
    Get the task status for a certain user and save 'em
    Args:
        user_id (str): The user id of the user
    """
    # lets first get the name of Employee
    emp_name = get("{}{}".format(base_url, user_id)).json().get("username")
    full_url = "{}{}/todos/".format(base_url, user_id)
    response = get(full_url, headers=headers).json()
    # save the tasks that belong to this user to a csv file
    file_name = "{}.json".format(user_id)
    task_dict_list = []

    for task in response:
        todo_dict = {}
        todo_dict.update({"task": task.get("title"),
                          "completed": task.get("completed"),
                         "username": emp_name})
        task_dict_list.append(todo_dict)

    try:
        with open(file_name, "w", encoding="utf-8") as json_file:
            dump({user_id: task_dict_list}, json_file)
    except Exception as e:
        return e.__cause__


if __name__ == "__main__":
    save_tasks_to_json(argv[1])
