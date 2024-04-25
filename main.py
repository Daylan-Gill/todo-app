import functions
import time

now = time.strftime("%d-%m-%Y %H:%M:%S")
print(f'{now} is the current date and time.')

while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1} - {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter a new to-do:")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Invalid input")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f'Todo "{todo_to_remove}" has been completed.'
            print(message)
        except IndexError:
            print("Invalid input")

    elif user_action.startswith("exit"):
        break

    else:
        print("Invalid input. Try again.")

print("Bye!")
