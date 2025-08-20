# todo.py
# Simple Todo List App (Command Line)

tasks = []

def show_tasks():
    if not tasks:
        print("\n✅ No tasks yet.")
    else:
        print("\n📝 Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(task):
    tasks.append(task)
    print(f"➕ Added: {task}")

def delete_task(index):
    try:
        removed = tasks.pop(index - 1)
        print(f"🗑️ Removed: {removed}")
    except IndexError:
        print("⚠️ Invalid task number.")

def main():
    while True:
        print("\nOptions: [1] Show [2] Add [3] Delete [4] Quit")
        choice = input("Enter choice: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            task = input("Enter new task: ")
            add_task(task)
        elif choice == "3":
            show_tasks()
            try:
                num = int(input("Enter task number to delete: "))
                delete_task(num)
            except ValueError:
                print("⚠️ Please enter a valid number.")
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Try again.")

if __name__ == "__main__":
    main()
