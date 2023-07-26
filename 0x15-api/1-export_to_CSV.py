#!/usr/bin/python3
"""
   A python script that fetches data from apis
"""

from sys import argv
import csv
import json
import requests


def main(id):
    """The main function """
    reqUsers = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
    reqTodos = requests.get(f'https://jsonplaceholder.typicode.com/todos')
    respUsers = json.loads(reqUsers.text)
    respTodos = json.loads(reqTodos.text)

    with open(f'{argv[1]}.csv', 'w', newline="") as csvfile:
        out = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in respTodos:
            if todo["userId"] == int(id):
                out.writerow([todo["userId"], respUsers["name"],
                              todo["completed"], todo["title"]])


if __name__ == "__main__":
    main(argv[1])
