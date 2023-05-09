#!/usr/bin/python3

"""
Query a subreddit and return the number of
total subscribers in that subredit
"""

from requests import get
from sys import argv


headers = {
    "User-Agent": "Of course I had to use a custom User-Agent",
    "X-Forwared-For": "iamthecavalry"
}


def number_of_subscribers(subreddit: str) -> int:
    """
    Query the subreddit and return the number of
    Active subs. If its an invalid subredit, return 0
    """
    response = get("https://www.reddit.com/r/{}/about.json".format(subreddit),
                   headers=headers)
    data = response.json()
    try:
        if 'error' in data.keys():
            return 0
        else:
            return data['data']['subscribers']
    except Exception as e:
        return 0


if __name__ == "__main__":
    print(number_of_subscribers(argv[1]))
