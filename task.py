
import json


class Task:
    def __init__(self, args, title, completed="False"):
        with open("data/task.json", "r") as file:
            data = json.load(file)
        
        self.id = len(data["tasks"]) + 1
        self.title = title
        self. completed = completed

    def mark_complete(self):
        self.completed = True
    
    def update_title(self, new_title):
        self.title = new_title


    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }

        
        
