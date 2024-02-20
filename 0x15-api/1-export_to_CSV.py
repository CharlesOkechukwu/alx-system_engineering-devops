#!/usr/bin/python3
"""Module using RESTFUL API to retrieve
tasks done by an employee"""
import requests
import sys


def to_csv(user_id):
    """get all records associated with a user id
    and return completed tasks"""
    url = "https://jsonplaceholder.typicode.com/"
    user_url = "{}users/{}".format(url, user_id)
    task_url = "{}/todos".format(user_url)

    user = requests.get(user_url).json()
    tasks = requests.get(task_url).json()
    uname = user.get("username")
    with open("{}.csv".format(user_id), 'w', encoding='utf-8') as f:
        for t in tasks:
            string = "'{}', '{}', '{}', '{}'\n"
            comp = t.get("completed")
            r = string.format(user_id, uname, comp, t.get("title"))
            f.write(r)


if __name__ == "__main__":
    to_csv(sys.argv[1])
