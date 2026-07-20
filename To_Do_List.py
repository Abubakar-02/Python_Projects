def add_task(task):
    with open("task.txt", "a", encoding="utf-8") as file:
        file.write(task+ "\n")
    print(f"✅ Task Added : {task}")

def view_tasks():
    with open("task.txt", "r", encoding="utf-8") as file:
        tasks=file.readlines()
    if len(tasks)==0:
        print("🧻 No Task Enter Yet")   
    else:
        print("\n 🧻 Your Tasks: ")
        for i , task in enumerate(tasks):
            print(f"{i+1}. {task.strip()}")    

def delete_task(task_number):
    with open("task.txt", "r", encoding="utf-8") as file:
        tasks=file.readlines()

    tasks.pop(task_number -1)

    with open("task.txt", "w", encoding="utf-8") as file:
       file.writelines(tasks)

    print("🗑️  Task deleted!")            



print("╔══════════════════════════════════╗")
print("║       📝 TO-DO LIST APP 📝       ║")
print("╚══════════════════════════════════╝")
print()

while True:
    print("1. Add Task")
    print("2. View all tasks")
    print("3. Remove Task")
    print("4. Exit")
    print()

    choice=input("Enter Your Choice (1-4): ")

    if choice == "1":
        task=input("Enter your Task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice =="3":
        view_tasks()
        task_num=int(input("Enter Your Task to Delete ! "))
        delete_task(task_num)
        print("\n✅ Updated Task List:")
        view_tasks()
    elif choice=="4":
        print("Good Bye 😊 ! Keep Completing 🏆 your Tasks 🧻📚 .")
        break