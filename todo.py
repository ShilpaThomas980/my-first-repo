def display_menu():
    print("\nTo-Do List Application")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")
    print()

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    print(f"Added..")


def view_task(tasks):
    if not tasks:
        print("Your to-do list is empty")
    else:
        print("\nYour To-Do List: ")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def remove_task(tasks):
    view_task(tasks)
    try: 
        task_number = int(input("Enter task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a Valid number")

def main():
    tasks = []
    display_menu()
    while True:
        choice = input("Choose (1-4): ")

        if choice == '1':
            add_task(tasks)
            print()
        elif choice == '2':
            view_task(tasks)
            print()
        elif choice == '3':
            remove_task(tasks)
            print()
        elif choice == '4' or choice.lower() in ['exit', 'esc', 'quit']:
            print("Exiting the application.Good Day!")
            print()
            break
        else:
            print("Invalid choice.")
            print()


if __name__ == "__main__":
    main()




