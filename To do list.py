# A To-Do List application is a useful project that helps users manage
# and organize their tasks efficiently. This project aims to create a
# command-line or GUI-based application using Python, allowing 
# users to create, update, and track their to-do lists.
class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task] = "Incomplete"
        print(f"Task '{task}' added to the to-do list.")

    def complete_task(self, task):
        if task in self.tasks:
            self.tasks[task] = "Complete"
            print(f"Task '{task}' marked as complete.")
        else:
            print(f"Task '{task}' not found in the to-do list.")

    def view_tasks(self):
        print("To-Do List:")
        for task, status in self.tasks.items():
            print(f"{task}: {status}")

def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. View Tasks")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter the task to mark as complete: ")
            todo_list.complete_task(task)
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
