#from dataclasses import dataclass
from datetime import datetime

# @dataclass
class Task:
    title: str = "New Task"
    desc: str = "New Description"
    done: bool = False
    time: datetime | None = None
    def __init__(self, title: str = "New Task", desc: str = "New Description", done: bool = False, time: datetime | None = None):
        self.title = title
        self.desc = desc
        self.done = done
        self.time = time
        
    def __repr__(self):
        return f"Task(title={self.title},desc={self.desc},done={self.done},time={self.time})"
    def __str__(self):
        return f"[{'x' if self.done else ' '}] {self.title} {f'{self.time}' if self.time is not None else ''}"
    
def print_tasks(tasks: list[Task]):
    for i,task in enumerate(tasks):
        print(i+1, task)