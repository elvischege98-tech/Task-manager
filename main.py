# Simple task utilities
_tasks = []  # list of dicts: {"title": str, "completed": bool}

def add_task(title: str):
    _tasks.append({"title": title, "completed": False})

def mark_task_complete(index: int) -> bool:
    if 0 <= index < len(_tasks):
        _tasks[index]["completed"] = True
        return True
    return False

def view_pending_tasks():
    return [t for t in _tasks if not t["completed"]]

def view_progress():
    total = len(_tasks)
    completed = sum(1 for t in _tasks if t["completed"])
    return completed, total


def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            add_task(title)
            print("Task added.")
        elif choice == "2":
            for i, t in enumerate(view_pending_tasks()):
                print(f"{i}. {t['title']}")
            idx = input("Enter the index of the task to mark complete: ")
            try:
                idx = int(idx)
                pending = view_pending_tasks()
                # Map index in pending list to overall tasks list
                if 0 <= idx < len(pending):
                    # find actual index
                    titles = [t['title'] for t in _tasks]
                    actual_index = titles.index(pending[idx]['title'])
                    if mark_task_complete(actual_index):
                        print("Task marked as complete.")
                    else:
                        print("Failed to mark task.")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "3":
            pending = view_pending_tasks()
            if not pending:
                print("No pending tasks.")
            else:
                for t in pending:
                    print(f"- {t['title']}")
        elif choice == "4":
            completed, total = view_progress()
            print(f"Progress: {completed}/{total} tasks completed")
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()