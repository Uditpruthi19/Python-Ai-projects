class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
        else:
            print("Invalid task index.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task description: ")
            task_manager.add_task(task)
            print("Task added.")

        elif choice == "2":
            task_manager.list_tasks()
            task_index = int(input("Enter task index to remove: ")) - 1
            task_manager.remove_task(task_index)
            print("Task removed.")

        elif choice == "3":
            task_manager.list_tasks()

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
