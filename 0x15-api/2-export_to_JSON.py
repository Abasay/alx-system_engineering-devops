#!/usr/bin/python3
"""
   A python script that fetches data from apis
"""

from sys import argv
import json
import requests


def main(id):
    """The main function """
    reqUsers = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
    reqTodos = requests.get(f'https://jsonplaceholder.typicode.com/todos')
    respUsers = json.loads(reqUsers.text)
    respTodos = json.loads(reqTodos.text)
    newTodos = []
    newDic = {}
    details = []
    completeDict = {}
    for i in range(0, len(respTodos)):
        if respTodos[i]["userId"] == int(id):
            newTodos.append(respTodos[i])
    for i in range(0, len(newTodos)):
        newDic["task"] = newTodos[i]["title"]
        newDic["completed"] = newTodos[i]["completed"]
        newDic["username"] = respUsers["username"]
        details.append(newDic.copy())
    completeDict = {id: details}
    with open(f'{id}.json', 'w') as myfile:
        json.dump(completeDict, myfile)


if __name__ == "__main__":
    main(argv[1])
