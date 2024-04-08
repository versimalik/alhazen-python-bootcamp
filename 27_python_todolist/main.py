from os import system, name
from time import sleep

todolist = [
    {
        'text' : 'Makan - makan',
        'status' : False
    },
    {
        'text' : 'Mancing',
        'status' : True
    },
]

def clearscreen():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def showTodolist():
    clearscreen()
    print("Todo List")
    print("=========")
    n = 1
    if len(todolist) < 1:
        print("EMPTY")
        print("Choose menu '2' to add new todo!")
    for todo in todolist:
        todo_status = "Done" if todo['status'] == True else "Not Done"
        print(f"{n}. {todo['text']} | {todo_status}")
        n+=1

def addNewTodo():
    showTodolist()
    print()
    print("What plan do you want to do?")
    new_todo = input()
    todolist.append(dict(text = new_todo, status = False))
    print(f"Todo {new_todo} is successfully added!")
    sleep(2)
    clearscreen()
    showTodolist()

def updateTodo():
    showTodolist()
    print()
    print("Which todo do you want to update?")
    todo_id=int(input("Input the number: "))
    try:
        selected_todo = todolist[todo_id-1]
        selected_todo_text = selected_todo['text']
        selected_todo_status_to = "Not Done" if selected_todo['status'] == True else "Done"
        confirmation = input(f"Are you sure want to update {selected_todo_text} to be {selected_todo_status_to}? y/N ")
        if confirmation.lower() == 'y':
            selected_todo['status'] = not selected_todo['status']
            print(f"{selected_todo_text} is updated!")
            sleep(2)
            showTodolist()
        else:
            showTodolist()
    except IndexError:
        print("Todo not found!")
        sleep(2)
        showTodolist()

def modifyTodo():
    showTodolist()
    print()
    print("Which todo do you want to modify?")
    todo_id=int(input("Input the number: "))
    try:
        selected_todo = todolist[todo_id-1]
        selected_todo_text = selected_todo['text']
        modify_to = input(f"What do you want to modify {selected_todo_text} to? ")
        confirmation = input(f"Are you sure want to modify {selected_todo_text} to be {modify_to}? y/N ")
        if confirmation.lower() == 'y':
            selected_todo['text'] = modify_to
            print(f"Todo is modified!")
            sleep(2)
            showTodolist()
        else:
            showTodolist()
    except IndexError:
        print("Todo not found!")
        sleep(2)
        showTodolist()

def deleteTodo():
    showTodolist()
    print()
    print("Which todo do you want to delete?")
    todo_id=int(input("Input the number: "))
    try:
        selected_todo = todolist[todo_id-1]
        selected_todo_text = selected_todo['text']
        confirmation = input(f"Are you sure want to delete {selected_todo_text}? y/N ")
        if confirmation.lower() == 'y':
            todolist.pop(todo_id-1)
            print(f"Todo is deleted!")
            sleep(2)
            showTodolist()
        else:
            showTodolist()
    except IndexError:
        print("Todo not found!")
        sleep(2)
        showTodolist()

title = "My Todo List"

print("=" * len(title))
print(title)
print("=" * len(title))

while True:
    print("""
Menu:
1. Show Todo List
2. Add New Todo List
3. Update Todo
4. Modify Todo
5. Delete Todo
x. Exit Application

Choose menu(1/2/3/4/5/x):""", end=" ")
    menu = input()

    if menu == "1":
        showTodolist()
    elif menu == "2":
        addNewTodo()
    elif menu == "3":
        updateTodo()
    elif menu == "4":
        modifyTodo()
    elif menu == "5":
        deleteTodo()
    elif menu == "x":
        print("See you next time!")
        sleep(3)
        clearscreen()
        break
    else:
        print("Wrong input!")