import os

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Loads the tasks from textfile."""
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as file:
                self.tasks = [task.strip() for task in file.readlines()]

    def save_tasks(self):
        """Saves tasks to a text file."""
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")
    def add_task(self, task):
        """Adds a new task in the list."""
        self.tasks.append(task)
        self.save_tasks()

    def delete_task(self, task_number):
        """Delete a task from the list."""
        try:
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' has been deleted.")
            self.save_tasks()
        except IndexError:
            print("Invalid!!!")

    def show_tasks(self):
        """Displays all tasks."""
        if not self.tasks:
            print("No task found!")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
