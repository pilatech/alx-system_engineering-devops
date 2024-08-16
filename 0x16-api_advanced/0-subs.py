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
        return (subr.get("data")
                .get("children")[0]
                .get("data")
                .get("subreddit_subscribers"))
    else:
        return 0
