#!/usr/bin/python3
"""Module Counting Subsribers on a Subreddit"""

import json
import requests


def number_of_subscribers(subreddit):
    """Get number of subscribers on a subreddit"""

    url = f"https://www.reddit.com/r/{subreddit}.json"
    res = requests.get(url)
    subr = json.loads(res.text)

    if (res.status_code == 200):
        if (res.url != url):
            return 0
        n = 0
        for child in subr.get("data").get("children"):
            n += child.get("data").get("subreddit_subscribers")
        return n
    else:
        return 0
