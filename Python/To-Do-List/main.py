from art import logo


class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_description):
        task_id = len(self.tasks) + 1
        self.tasks[task_id] = {"description": task_description, "completed": False}
        print(f"Task {task_id} added: {task_description}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for task_id, task in self.tasks.items():
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{task_id}: {task['description']} ({status})")

    def update_task(self, task_id, new_description):
        if task_id in self.tasks:
            self.tasks[task_id]["description"] = new_description
            print(f"Task {task_id} updated: {new_description}")
        else:
            print(f"Task {task_id} not found in the to-do list.")

    def mark_completed(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id]["completed"] = True
            print(f"Task {task_id} marked as completed.")
        else:
            print(f"Task {task_id} not found in the to-do list.")

    def run(self):
        print(logo)
        should_continue = True
        while should_continue:
            print("\nOptions:")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Update Task")
            print("4. Mark Task as Completed")
            print("5. Quit")
            choice = input("Enter your choice (1/2/3/4/5): ")

            if choice == "1":
                task_description = input("Enter task description: ")
                self.add_task(task_description)
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                task_id = int(input("Enter task ID to update: "))
                new_description = input("Enter new task description: ")
                self.update_task(task_id, new_description)
            elif choice == "4":
                task_id = int(input("Enter task ID to mark as completed: "))
                self.mark_completed(task_id)
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()
