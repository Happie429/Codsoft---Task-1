todo_list = []

def show_menu():
    print("1.View\n2.Add\n3.Update\n4.Delete\n5.Done\n6.Exit")

def view_tasks():
    if not todo_list:
        print("No tasks.")
    else:
        for i, task in enumerate(todo_list,1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}.{task['task']} [{status}]")

def add_task():
    task = input("New task:")
    todo_list.append({"task":task,"done":False})
    print("Addded.")

def update_task():
    view_tasks()
    try:
        i=int(input("task number to update: ")) - 1
        todo_list[i]["task"] = input("New task:")
        print("Updated.")
    except:
        print("Invalid.")

def delete_task():
    view_tasks()
    try:
        i = int(input("Task number to delete:")) - 1
        print(f"Deleted : {todo_list.pop(i)['task']}")
    except:
        print("Inavalid.")


def mark_done():
    view_tasks()
    try:
        i=int(input("Task number to mark done:")) - 1
        todo_list[i]["Done"] = True
        print("Marked done.")
    except:
        print("Invalid.")

while True:
    show_menu()
    choice = input("Choose(1-6):")
    if choice == '1': view_tasks()
    elif choice == '2': add_task()
    elif choice == '3': update_task()
    elif choice == '4': delete_task()
    elif choice == '5':mark_done()
    elif choice == '6':
        print("Goodbye!")
        break
    else: print("Try gain.")




