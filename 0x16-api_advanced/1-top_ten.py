#!/usr/bin/python3

"""
query the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

from requests import get
from sys import argv


def top_ten(subreddit: str) -> None:
    """
    function that does the heavy lifting for us
    Args:
        subreddit (str) -> The subreddit to query
    Returns: The top 10 hots for that subreddit
    """
    headers = {
        "User-Agent": "Marvel's Agents of Shield/21",
        "X-Forwared-For": "Phil J. Coulson"
    }

    request_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    try:
        response = get(request_url, headers=headers,
                       allow_redirects=False).json()
        data = response['data']['children']
        [print(post['data']['title']) for post in data[:10]]
    except Exception:
        print("None")


if __name__ == "__main__":
    (top_ten(argv[1]))
