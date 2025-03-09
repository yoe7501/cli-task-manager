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
    return args

def check_action(args: List[str], file_path):
    match(args[1]):
        case "-add":
           return add_task(file_path, args[2])
        case "-remove":
            return remove_task(file_path, args[2])
        case "-update":
            return update_task(file_path, args[2], args[3])
        case "-show":
            return show_task(file_path)
        case "-complete":
            return complete_task(file_path, args[2])
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

    task = Task(sys.argv, new_task)

    data["tasks"].append(task.to_dict())

    with open(file_path, "w") as file:
        json.dump(data, file, indent = 4)

def remove_task(file_path, id: str):
    new_list = []

    with open(file_path, "r") as file:
        data = json.load(file)
    
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
    
    for task in data["tasks"]:
        if task["id"] == f"{id}":
            task["completed"] = "True"
        new_list.append(task)

    with open(file_path, "w") as file:
        json.dump({"tasks": new_list},file)



if __name__ == "__main__":
    main()
#1. be able to add new task 
#2. only be able to do one thing at a time 
#3. show progress when something is changed or option is given
#4. be able to edit a task on the list 
#5. be able to delete task on a list 
#6. store all data in json file.
#7 lists should be always odd as every opotion should have a matching description 
# of sorts plus the file argument

