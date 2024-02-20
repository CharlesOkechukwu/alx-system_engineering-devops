#!/usr/bin/python3
"""Module using RESTFUL API to retrieve
tasks done by an employee"""
import requests
import sys


def get_records(user_id):
    """get all records associated with a user id
    and return completed tasks"""
    url = "https://jsonplaceholder.typicode.com/"
    user_url = "{}users/{}".format(url, user_id)
    task_url = "{}/todos".format(user_url)

    user = requests.get(user_url).json()
    tasks = requests.get(task_url).json()  
    comp = [t.get("title") for t in tasks if t.get("completed")]
    name = user.get("name")
    string = "Employee {} is done with tasks({}/{}):"
    print(string.format(name, len(comp), len(tasks)))
    for t in comp:
        print("\t {}".format(t))


if __name__ == "__main__":
    get_records(sys.argv[1])
