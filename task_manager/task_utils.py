from validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

tasks = []


def add_task(title, description, due_date):
    if not validate_task_title(title):
        return

    if not validate_task_description(description):
        return

    if not validate_due_date(due_date):
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")


def mark_task_as_complete(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Error: Invalid task index.")


def view_pending_tasks():
    pending_tasks = [
        task for task in tasks
        if not task["completed"]
    ]

    return pending_tasks


def calculate_progress():
    if len(tasks) == 0:
        return 0

    completed = sum(
        1 for task in tasks
        if task["completed"]
    )

    return (completed / len(tasks)) * 100