#!/usr/bin/python3

"""
Queries the Reddit API recursively and returns
a list containing the titles of all hot articles
for a given subreddit. If no results are found for
the given subreddit, return None.
"""

from requests import get
from sys import argv


def recurse(subreddit: str, hot_list=[], after="", count=0) -> list:
    """Function to recurcively query a subreddit
    And return the hot topics for the subreddit
    Args:
        subreddit (str): The subreddit to query
        hot_list (list): Doesn't have to be passed
        after (str): Doesn't have to be passed
        count (int): Doesn't have to be passed
    """
    headers = {
        "User-Agent": "I'll use a real user Agent this time. I promise", 
        "X-Forwarded-For": "$(whoami)"
    }
    query_strings = {
        "after": after,
        "count": count,
        "limit": 100
    }
    request_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    response = get(request_url, headers=headers, params=query_strings, allow_redirects=False)

    if response.status_code == 404