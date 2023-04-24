#!/usr/bin/env python3

"""A module to make API calls to a mockup API server and print the responses to standard output.

Usage:
./0-gather-data_from_an_API.py <ID>

Where <ID> is the employee ID for whom we want to list the tasks.
"""

import pathlib
import requests
import sys


API_BASE_URL = "https://jsonplaceholder.typicode.com"


def get_tasks(user_id: str) -> None:
    """
    Get the task status for a certain user and save the results to a CSV file.
    
    Args:
        user_id (str): The user id of the user.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/users/{user_id}")
        response.raise_for_status()
        emp_name = response.json().get("name")

        response = requests.get(f"{API_BASE_URL}/users/{user_id}/todos/", headers={"User-Agent": "Thing Gecko/20100101 Firefox/102.0"})
        response.raise_for_status()

        tasks = response.json()
        filename = pathlib.Path(f"{user_id}.csv")

        with filename.open("w", encoding="utf-8") as csv_file:
            for task in tasks:
                line_content = f'"{user_id}", "{emp_name}", "{task["completed"]}", "{task["title"]}"'
                csv_file.write(line_content + "\n")

    except (requests.exceptions.HTTPError, requests.exceptions.RequestException) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <ID>", file=sys.stderr)
        sys.exit(1)

    user_id = sys.argv[1]
    get_tasks(user_id)
