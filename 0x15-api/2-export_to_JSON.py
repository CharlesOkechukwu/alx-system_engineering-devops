#!/usr/bin/python3
"""Module using RESTFUL API to retrieve
tasks done by an employee"""
import json
import requests
import sys


def to_json(user_id):
    """get all records associated with a user id
    and return completed tasks"""
    url = "https://jsonplaceholder.typicode.com/"
    user_url = "{}users/{}".format(url, user_id)
    task_url = "{}/todos".format(user_url)

    user = requests.get(user_url).json()
    tasks = requests.get(task_url).json()
    uname = user.get("username")
    with open("{}.json".format(user_id), 'w', encoding='utf-8') as f:
        record = {user_id: []}
        for t in tasks:
            comp = t.get("completed")
            r = {"task": t.get("title"), "completed": comp,
                 "username": uname}
            record[user_id].append(r)
        f.write(json.dumps(record))


if __name__ == "__main__":
    to_json(sys.argv[1])
