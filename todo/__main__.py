from todo.lib import Task, print_tasks, __repr__

tasks:list[Task] = []
while True:
    print_tasks(tasks)
    choice = int(input("[1] Create a new task\n[2] Mark task as complete\n[3] Edit task\n[4] Delete task\n[5] Remove all complete tasks\n[6] View task"))
    
    if choice == 1:
        tasks.append(Task())
        # title = input("Enter new title (leave empty to not change): ")
        # desc = input("Enter new desc (leave empty to not change): ")
        # date = input("Enter new date (mm/dd/yyyy) (leave empty to not change): ")
        # index = int(len(tasks) - 1)
        # tasks[index].update(title, desc, date)
    elif choice == 2:
        index = int(input("Enter task index"))
        tasks[index-1].done = True
    elif choice == 3:
        index = int(input("Enter task index: "))
        title = input("Enter new title (leave empty to not change): ")
        desc = input("Enter new desc (leave empty to not change): ")
        date = input("Enter new date (dd/mm/yy) (leave empty to not change): ")
        
        tasks[index-1].update(title, desc, date)
    elif choice == 4:
        index = int(input("Enter index of task to delete"))
        tasks.remove(index-1)
    elif choice == 5:
        tasks = [t for t in tasks if not t.done]
    elif choice == 6:
        index = int(input("Enter task index"))
        print(tasks[index-1].__repr__())
                       
                       
                       
                     
