import json
import os
import sys
from task import Task
from typing import List

def main () :
    file_path = "data/task.json"
    create_json(file_path)
    args = read_args()
    check_action(args, file_path)
    return 0

def create_json(filepath):
    if not os.path.exists(filepath):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w") as file:
            json.dump({"tasks": []}, file)


def read_args() -> List[str]:
    args: List[str] = sys.argv
    if len(args) > 4:
        print("To many argument remember to quote around string")
        exit()
    return args

def check_action(args: List[str], file_path):

    match(args[1]):
        case "-add":
           if len(args) > 3:
               print("Usage: python3 -m cli-task-manager.py -add 'task title'")
           return add_task(file_path, args[2])
        case "-remove":
            if len(args) > 3:
               print("Usage: python3 -m cli-task-manager.py -remove 1")
            return remove_task(file_path, args[2])
        case "-update":
            if len(args) > 4:
               print("Usage: python3 -m cli-task-manager.py -update 1 'task title'")
            return update_task(file_path, args[2], args[3])
        case "-show":
            if len(args) > 2:
               print("Usage: python3 -m cli-task-manager.py -show")
            return show_task(file_path)
        case "-complete":
            if len(args) > 3:
               print("Usage: python3 -m cli-task-manager.py -complete 2")
            return complete_task(file_path, args[2])
        case "-help":
            if len(args) > 2:
               print("Usage: python3 -m cli-task-manager.py -help")
            return help()
        case _:
            return "python3 -m cli-task-manager.py [-add, -remove, -update, -show] []"

def show_task(file_path):
    
    with open(file_path, "r") as file:
        data = json.load(file)

    for task in data["tasks"]:
        print("----------------------------------------------------------------------")
        print(f"{task["id"]}: {task["title"]} | Complete: {task["completed"]}")
        print("----------------------------------------------------------------------")


def add_task(file_path, new_task):
    with open(file_path, "r") as file:
        data = json.load(file)

    task = Task(new_task)

    data["tasks"].append(task.to_dict())

    with open(file_path, "w") as file:
        json.dump(data, file, indent = 4)

def remove_task(file_path, id: str):
    new_list = []

    with open(file_path, "r") as file:
        data = json.load(file)
    
    if int(id) > len(data["tasks"]):
        print("id not valid")
        exit()
    
    for task in data["tasks"]:
        if task["id"] != id:
            new_list.append(task)
    
    # renubmer id
    i = 1
    for task in new_list:
        task["id"] = f"{i}"
        i += 1
    with open(file_path, "w") as file:
        json.dump({"tasks": new_list}, file)

def update_task(file_path, id, new_task):
    new_list = []
    with open(file_path, "r") as file:
        data = json.load(file)

    if int(id) > len(data["tasks"]):
        print("id not valid")
        exit()

    for task in data["tasks"]:
        if task["id"] == f"{id}":
            task["title"] = new_task
        
        new_list.append(task)
    with open(file_path, "w") as file:
        json.dump({"tasks": new_list}, file)

    
    
def complete_task(file_path, id):
    new_list = []
    with open(file_path, "r") as file:
        data = json.load(file)
    
    if int(id) > len(data["tasks"]):
        print("id not valid")
        exit()

    for task in data["tasks"]:
        if task["id"] == f"{id}":
            task["completed"] = "True"
        new_list.append(task)

    with open(file_path, "w") as file:
        json.dump({"tasks": new_list},file)

def help():
    print("Task Manager CLI - Available Commands:")
    print("------------------------------------------------")
    print("python3 -m cli-task-manager.py -add 'task title'    : Adds a new task with the given title.")
    print("python3 -m cli-task-manager.py -remove <task_id>    : Removes the task with the specified ID.")
    print("python3 -m cli-task-manager.py -update <task_id> 'new title' : Updates the title of the task with the specified ID.")
    print("python3 -m cli-task-manager.py -show                 : Shows all tasks in the task manager.")
    print("python3 -m cli-task-manager.py -complete <task_id>   : Marks the task with the specified ID as complete.")
    print("python3 -m cli-task-manager.py -help                 : Displays this help message.")
    print("------------------------------------------------")




if __name__ == "__main__":
    main()


