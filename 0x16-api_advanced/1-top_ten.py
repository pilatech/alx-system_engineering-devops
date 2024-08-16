#!/usr/bin/python3
"""Module printing top 10 articles on a Subreddit"""

import json
import requests


def top_ten(subreddit):
    """Get top 10 articles on a subreddit"""

    url = f"https://www.reddit.com/r/{subreddit}.json"
    res = requests.get(url)
    subr = json.loads(res.text)

    if (res.status_code == 200):
        if (res.url != url):
            print(None)
            return
        mx = 10
        articles = subr.get("data").get("children")
        if len(articles) < 10:
            mx = len(articles)
        for i in range(mx):
            print(articles[i].get("data").get("title"))
    else:
        print(None)
