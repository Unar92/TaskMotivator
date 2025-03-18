import json
import os
import datetime
import random

# File to store tasks
TASK_FILE = "tasks.json"

# Motivational quotes
QUOTES = [
    "You’ve got this! One step at a time.",
    "Progress, not perfection.",
    "Keep going—every task completed is a win!",
    "The best way to get started is to quit talking and begin doing.",
]

# Load tasks from file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task():
    task_name = input("Enter task name: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    try:
        due = datetime.datetime.strptime(due_date, "%Y-%m-%d")
        task = {
            "name": task_name,
            "due_date": due_date,
            "completed": False
        }
        tasks = load_tasks()
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task '{task_name}' added!")
    except ValueError:
        print("Invalid date format! Use YYYY-MM-DD.")

# View all tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet!")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. {task['name']} (Due: {task['due_date']}) [{status}]")
    check_reminders(tasks)

# Mark task as complete
def complete_task():
    view_tasks()
    tasks = load_tasks()
    if not tasks:
        return
    try:
        task_num = int(input("Enter task number to mark complete: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["completed"] = True
            save_tasks(tasks)
            print(f"Task '{tasks[task_num]['name']}' marked as complete!")
            print(get_motivational_quote())
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# Check for reminders
def check_reminders(tasks):
    today = datetime.datetime.now()
    for task in tasks:
        if not task["completed"]:
            due = datetime.datetime.strptime(task["due_date"], "%Y-%m-%d")
            if due <= today:
                print(f"REMINDER: '{task['name']}' is overdue!")
            elif (due - today).days <= 1:
                print(f"REMINDER: '{task['name']}' is due soon!")

# Get a random motivational quote
def get_motivational_quote():
    return random.choice(QUOTES)

# Main menu
def main():
    while True:
        print("\n=== TaskMotivator ===")
        print(get_motivational_quote())
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            print("See you later—stay motivated!")
            break
        else:
            print("Invalid option, try again!")

if __name__ == "__main__":
    main()