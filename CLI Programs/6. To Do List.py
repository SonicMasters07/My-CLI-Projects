import os

class Task:
    storage = {"Groceries": ["Apple-Milk-Flour-Biscuits", "28-9-2025", "High", False] }

    def __init__(self,name,description,due_date,priority,completed):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = completed

    def task_add(self):
        Task.storage[self.name] = [self.description, self.due_date, self.priority, self.completed]
    
    def all_task_view(self,):
        for name,details in Task.storage.items():
            print(f"""Name of Task is {name}
Description: {details[0]}
Due_Date: {details[1]}
Priority: {details[2]}
Completed: {details[3]}
----------------------
""")
            
    def search_task(self, task_name):
            if task_name in Task.storage:
                details = Task.storage[task_name]
                print(f"Name: {task_name}\nDescription: {details[0]}\nDue: {details[1]}\nPriority: {details[2]}\nCompleted: {details[3]}")
            else:
                print("Task not found")
    
    def task_update(self, task_name):
        if task_name in Task.storage:
            print("Previous Information of Task")
            print(Task.storage[task_name])
            print("Update Information")
            description = input("Give a description: ")
            due_date = input("Give a Due_Date: ")
            priority = input("Set priority: ")
            Task.storage[task_name][0] = description
            Task.storage[task_name][1] = due_date
            Task.storage[task_name][2] = priority
            Task.storage[task_name][3] = False
            print("Task Updated")


        else:
                print("Task not found")
    
    def task_delete(self,task_name):
        if task_name in Task.storage:
            Task.storage.pop(task_name)
            print("Task deleted")
        else:
            print("Task not Found")
            
    def task_completed(self, com):
        if com in Task.storage:
            Task.storage[com][3] = True
            print("Status Changed")
        else:
            print("Task not found")


def terminal():
    T = Task("Dummy","Dummy","01-01-2000","Low",False)
    keys = ""
    loop = True
    while loop :
        print("""1. Add Task
2. View all Tasks
3. Search Task
4. Update Task
5. Mark Task as Complete
6. Delete Task
7. Exit
""")
        keys = input("Which option you want to choose: ")
        os.system("cls")
        if keys == "1":
            name = input("Name of Task: ").upper()
            description = input("Give a description: ")
            due_date = input("Give a Due_Date: ")
            priority = input("Set priority: ")
            completed = False
            N_T = Task(name,description,due_date,priority,completed)
            N_T.task_add()
            print("Task has been added")
            input("Press enter to continue...")
            os.system("cls")
        
        if keys == "2":
            os.system("cls")
            T.all_task_view()
            input("Press enter to continue...")
            os.system("cls")

        if keys == "3":
            task_name = input("Which task you want to find: ").upper()
            T.search_task(task_name)
            input("Press enter to continue...")
            os.system("cls")

        if keys == "4":
            task_name = input("Which task you want to update: ").upper()
            T.task_update(task_name)
            input("Press enter to continue...")
            os.system("cls")

        if keys == "5":
            com = input("What task has been completed: ").upper()
            T.task_completed(com)
            input("Press enter to continue...")
            os.system("cls")

        if keys == "6":
            task_name = input("Which task you want to delete: ").upper()
            T.task_delete(task_name)
            input("Press enter to continue...")
            os.system("cls")

        if keys == "7":
            break

def main():
    os.system("cls")
    terminal()

main()