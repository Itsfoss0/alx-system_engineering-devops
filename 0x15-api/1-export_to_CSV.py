#!/usr/bin/python3
"""A simple module to make API Calls
To a mockup API server and return the
Responses. Then print them out to standard output
Usage: ./0-gather-data_from_an_API <ID>
Where <ID> is the employee ID for whom we want to list
The tasks"""

from requests import get
from sys import argv

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "Thing Gecko/20100101 Firefox/102.0"
}
base_url = "https://jsonplaceholder.typicode.com/users/"


def save_task_status_to_csv(user_id: str) -> None:
    """
    Get the task status for a certain user and save 'em
    Args:
        user_id (str): The user id of the user
    """
    # lets first get the name of Employee
    emp_name = get("{}{}".format(base_url, user_id)).json().get("name")
    full_url = "{}{}/todos/".format(base_url, user_id)
    response = get(full_url, headers=headers).json()
    # save the tasks that belong to this user to a csv file
    file_name = "{}.csv".format(user_id)
    with open(file_name, "w", encoding="utf-8") as csv_file:
        for resp in response:
            csv_file.write('"{}","{}","{}","{}"\n'
                           .format(resp.get("userId"),
                                   emp_name, resp.get("completed"),
                                   resp.get("title")))


if __name__ == "__main__":
    save_task_status_to_csv(argv[1])
