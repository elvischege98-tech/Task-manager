from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress,
    tasks
)


def main():
    while True:
        print("\n===== TASK MANAGEMENT SYSTEM =====")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")

            add_task(title, description, due_date)

        elif choice == "2":
            pending = view_pending_tasks()

            if not pending:
                print("No pending tasks.")
                continue

            for i, task in enumerate(pending):
                print(f"{i}. {task['title']}")

            try:
                index = int(input("Enter task index to mark complete: "))

                # map pending index → actual task index
                actual_index = tasks.index(pending[index])

                mark_task_as_complete(actual_index)

            except (ValueError, IndexError):
                print("Error: Invalid task index.")

        elif choice == "3":
            pending = view_pending_tasks()

            if not pending:
                print("No pending tasks.")
            else:
                for task in pending:
                    print(f"- {task['title']} | {task['due_date']}")

        elif choice == "4":
            print(calculate_progress(tasks))

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()