#!/usr/bin/python3
"""
   A python script that fetches data from apis
"""

from sys import argv
import json
import requests

def main():
    """The main function """
    reqUsers = requests.get(f'https://jsonplaceholder.typicode.com/users')
    reqTodos = requests.get(f'https://jsonplaceholder.typicode.com/todos')
    respUsers = json.loads(reqUsers.text)
    respTodos = json.loads(reqTodos.text)
    newTodos = []
    newDic = {}
    details = []
    completeDict = {}
    all_users = {}
    all_list = []
    numberOfUsers = len(respUsers) + 1

    for i in range(1, numberOfUsers):
        for todos in respTodos:
            if todos["userId"] == i:
                newTodos.append(todos)
        for j in range(0, len(newTodos)):
            newDic["username"] = respUsers[i - 1]["username"]
            newDic["task"] = newTodos[j]["title"]
            newDic["completed"] = newTodos[j]["completed"]
            details.append(newDic.copy())
        completeDict = {i : details}
        all_list.append(i : details)
        newTodos = []
        details = []
    with open('todo_all_employees.json', 'w') as f:
        json.dump(all_list, f)


if __name__ == "__main__":
    main()
