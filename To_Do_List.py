# Simple To do list program
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f'Task added: "{task}"')

    def view(self):
        if not self.tasks:
            print("List is empty.")
            return
        for index, task in enumerate(self.tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f'{index}. {task["task"]} [{status}]')

    def mark_as_completed(self, task_index):
        if 0 < task_index <= len(self.tasks):
            self.tasks[task_index - 1]["completed"] = True
            print(f'Task {task_index} marked as completed.')
        else:
            print("List is empty.")

    def remove(self, task_index):
        if 0 < task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f'Task removed: "{removed_task["task"]}"')
        else:
            print("List is empty")

def main():
    todo_list = ToDoList()
    
    while True:
        print("\nTo-Do List ")
        print("---------------------------------")
        print("** Menu **")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit")
        print("---------------------------------")
        
        ch = input("Enter your choice:")
        print("------------------------------------")
        
        if ch == '1':
            task = input("Enter the task: ")
            todo_list.add(task)
        elif ch == '2':
            todo_list.view()
        elif ch == '3':
            task_index = int(input("Enter task number to mark as completed: "))
            todo_list.mark_as_completed(task_index)
        elif ch == '4':
            task_index = int(input("Enter task number to remove: "))
            todo_list.remove(task_index)
        elif ch == '5':
            print("Exiting...Thank You.....!")
            break
        else:
            print("Please enter the valid choice..!")

if __name__ == "__main__":
    main()
