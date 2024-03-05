#!/usr/bin/python3
"""module to get number of sybscribers to
reddit using an api"""
import requests


def number_of_subscribers(subreddit):
    """function to get number of subscribers to a subreddit
    using reddit api
    return: 0 if subreddit is invalid
    number of subscribers"""
    link = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    subs = 0
    header = {'User-Agent': 'api-advanced/v1.0.0 by Charles'}
    res = requests.get(url=link, headers=header, allow_redirects=False)
    if res.status_code == 200:
        result = res.json().get('data')
        subs = result["subscribers"]
    return subs
