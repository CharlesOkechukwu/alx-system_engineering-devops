#!/usr/bin/python3
"""Module using RESTFUL API to retrieve
tasks done by an employee"""
import json
import requests


def to_all_json():
    """get all records associated with a user id
    and return completed tasks"""
    url = "https://jsonplaceholder.typicode.com/"
    users_url = "{}users".format(url)
    record = {}
    users = requests.get(users_url).json()
    for u in users:
        u_data = []
        user_url = "{}users/{}".format(url, u["id"])
        task_url = "{}/todos".format(user_url)
        tasks = requests.get(task_url).json()
        for t in tasks:
            comp = t.get("completed")
            r = {"username": u.get("username"),
                 "task": t.get("title"), "completed": comp}
            u_data.append(r)
        record.update({u["id"]: u_data})
    with open("todo_all_employees.json", 'w', encoding="utf-8") as f:
        f.write(json.dumps(record))


if __name__ == "__main__":
    to_all_json()
