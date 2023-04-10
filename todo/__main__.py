from todo.lib import Task, print_tasks

tasks:list[Task] = []
while True:
    print_tasks(tasks)
    choice = int(input("[1] Create a new task\n[2] Mark task as complete\n[3] Edit task"))
    
    if choice == 1:
        tasks.append(Task())
    elif choice == 2:
        index = int(input("Enter task index"))
        tasks[index-1].done = True
    elif choice == 3:
        title = input("Enter new title (leave empty to not change): ")
        desc = input("Enter new desc (leave empty to not change): ")
        date = input("Enter new date (mm/dd/yyyy) (leave empty to not change): ")
        
        task.update(title, desc, date)
