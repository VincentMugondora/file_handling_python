to_do = ["Buy Groceries", "Clean House", "Cook Dinner", "Wash Car", "Walk Dog"]

def get_tasks():
    for task in to_do:
        print(task)

def add_task():
    task = input("Enter a task: ")
    to_do.append(task)

def remove_task():
    task = input("Enter a task to remove: ")
    if task in to_do:
        to_do.remove(task)
        print(f"Task '{task}' removed.")
    else:
        print("Task not found.")
        
def menu():
    print("1. Get tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Quit")
    choice = input("Enter your choice: ")
    return choice
    
def main():
    menu()

    while True:
        choice = menu()
        if choice == "1":
            get_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()