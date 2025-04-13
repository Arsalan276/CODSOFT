def To_Do_List():
    tasks=[]
    while True:
        print("Add New Task Press(1)")
        print("View Task Status Press(2)")
        print("Update the Task Status Press(3)")
        print("Delete the Task Press(4)")
        print("Exit(5)")
        print("\n")

        choice=input("Select the option from above\n")

        if choice=='1':
            task=input("Enter the new task or upcoming task\n")
            tasks.append({"task":task,"completed" :False})
            print(f"Task '{task}' added successfully\n")
        elif choice=='2':
            if not tasks:
                print("No Tasks are available to view\n")
            else:
                for idx, task in enumerate(tasks,1):
                    status="Done" if task["completed"] else "Not Completed yet"
                    print(f"{idx}.[{status}] {task['task']}")
                    print("\n")
        elif choice=='3':
            if not tasks:
                print("No Tasks are available to update\n")
            else:
                for idx, task in enumerate(tasks,1):
                    print(f"{idx}. {task['task']}")
                try:
                    task_num=int(input("Enter the task number to update the status\n"))-1 # Because default indexing start from 0 so to avoid unexpected selection or modification as seen before we should stubtract -1
                    if 0<=task_num<len(tasks):
                        tasks[task_num]["completed"]=True
                        print(f"Task '{tasks[task_num]['task']}' has been marked as completed\n")
                    else:
                        print("Invalid Task number")
                except ValueError:
                    print("You Entered wrong value")
        elif choice=='4':
            if not tasks:
                print("No Tasks are available to delete\n")
            else:
                for idx, task in enumerate(tasks,1):
                    print(f"{idx}. {task['task']}")
                try:
                    task_delete=int(input("\nEnter the task number to delete from the list\n"))-1
                    if 0<=task_delete<len(tasks):
                        deleted_task=tasks.pop(task_delete)
                        print(f"Task '{deleted_task['task']}' has been deleted\n")
                    else:
                        print("Invalid Task number")
                except ValueError:
                    print("You Entered wrong value")
        elif choice=='5':
            print("Goodbye")
            break
        else:
            print("UnExpected error")

if __name__ == '__main__': # this should be correct syntax wise to call the function
    To_Do_List()