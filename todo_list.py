import os

TODO_FILE = 'todo.txt'

def show_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            todos = file.readlines()
            if todos:
                print("Your To-Do List:")
                for idx, todo in enumerate(todos, 1):
                    print(f"{idx}. {todo.strip()}")
            else:
                print("Your To-Do List is empty.")
    else:
        print("Your To-Do List is empty.")

def add_todo():
    todo = input("Enter a new to-do item: ")
    with open(TODO_FILE, 'a') as file:
        file.write(todo + '\n')
    print(f"Added: {todo}")

def delete_todo():
    show_todos()
    index = int(input("Enter the number of the to-do item to delete: "))
    with open(TODO_FILE, 'r') as file:
        todos = file.readlines()
    if 0 < index <= len(todos):
        removed = todos.pop(index - 1)
        with open(TODO_FILE, 'w') as file:
            file.writelines(todos)
        print(f"Deleted: {removed.strip()}")
    else:
        print("Invalid number.")

def main():
    while True:
        print("\nTo-Do List App")
        print("1. Show To-Do List")
        print("2. Add To-Do Item")
        print("3. Delete To-Do Item")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            show_todos()
        elif choice == '2':
            add_todo()
        elif choice == '3':
            delete_todo()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
