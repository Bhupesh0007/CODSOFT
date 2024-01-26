import os

# Function to display the menu
def display_menu():
    print("===== To-Do List App =====")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Exit")

# Function to display tasks
def display_tasks():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        if tasks:
            print("Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")
        else:
            print("No tasks in the list.")

# Function to add a task
def add_task():
    task = input("Enter the task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully.")

# Function to complete a task
def complete_task():
    display_tasks()
    task_number = int(input("Enter the task number to complete: "))
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    if 1 <= task_number <= len(tasks):
        del tasks[task_number - 1]
        with open("tasks.txt", "w") as file:
            file.writelines(tasks)
        print("Task completed.")
    else:
        print("Invalid task number.")

# Main function
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    if not os.path.exists("tasks.txt"):
        open("tasks.txt", "w").close()  # Create tasks file if not exists
    main()
