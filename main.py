from manage_myTask import TaskManager

def display_menu():
    """Display options."""
    print("\nTask Manager")
    print("1. View my Tasks")
    print("2. Add new Task")
    print("3. Delete a Task")
    print("4. Exit")

def main():
    task_manager = TaskManager()

    while True:
        display_menu()
        choice = input("Choose any option (1-4): ")

        if choice == "1":
            task_manager.show_tasks()

        elif choice == "2":
            task = input("Enter your task to add: ")
            task_manager.add_task(task)
            print(f"Task '{task}' has been added!!")

        elif choice == "3":
            task_manager.show_tasks()
            try:
                task_number = int(input("Enter the task number to delete: "))
                task_manager.delete_task(task_number)
            except ValueError:
                print("Enter a valid num.")

        elif choice == "4":
            print("Tata!!")
            break

        else:
            print("Invalid choice!!")

if __name__ == "__main__":
    main()
