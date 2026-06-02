from datetime import datetime

def validate_task_title(title):
    if not isinstance(title, str) or len(title.strip()) == 0:
        raise ValueError("Task title cannot be empty.")
    return True


def validate_task_description(description):
    if not isinstance(description, str) or len(description.strip()) == 0:
        raise ValueError("Task description cannot be empty.")
    return True


def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        raise ValueError("Invalid due date format. Use YYYY-MM-DD")