#!/usr/bin/python3
"""module: list ten top titles of posts
popular under subreddit"""
import requests


def top_ten(subreddit):
    """list top ten titles under a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': "api-advanced/1.0.0"}
    limit = {'limit': '10'}
    res = requests.get(url, headers=headers, params=limit,
                       allow_redirects=False)
    if res.status_code == 200:
        result = res.json().get('data')
        titles = [c['data']['title'] for c in result['children']]
        for title in titles:
            print(title)
    else:
        print("None")
