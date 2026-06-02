from task_manager.validation import (
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

    tasks.append({
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    })

    print("Task added successfully!")


def mark_task_as_complete(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Error: Invalid task index.")


def view_pending_tasks():
    return [t for t in tasks if not t["completed"]]


# ✅ FIXED: now accepts parameter AND works with tests
def calculate_progress(task_list):
    if len(task_list) == 0:
        return 0.0

    completed = sum(1 for t in task_list if t["completed"])
    return (completed / len(task_list)) * 100