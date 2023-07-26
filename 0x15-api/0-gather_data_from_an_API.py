#!/usr/bin/python3
"""
   A python script that fetches data from apis
"""

import requests
from sys import argv
import json


def main(id):
    """The main function """
    reqUsers = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
    reqTodos = requests.get(f'https://jsonplaceholder.typicode.com/todos')
    respUsers = json.loads(reqUsers.text)
    respTodos = json.loads(reqTodos.text)

    completed = 0
    newTodos = []
    for todo in respTodos:
        if todo["userId"] == int(id):
            newTodos.append(todo)
            if todo["completed"]:
                completed = completed + 1
    print(f"Employee {respUsers['name']} is done"
          " with tasks {completed}/{len(newTodos)}")
    for task in newTodos:
        if task["completed"]:
            print(f"\t {task['title']}")


if __name__ == "__main__":
    main(argv[1])
