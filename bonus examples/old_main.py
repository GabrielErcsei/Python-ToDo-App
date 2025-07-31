index_updater = 1
todo_list = []

def display_to_do_list(todos: list):
    for index, item in enumerate(todos):
        print(f"{index + index_updater}-{item}")


while True:
    user_input_action = input("Type add, show, edit, complete or exit to interact withe the to do list: ").strip()
    match user_input_action:
        case "add":
            todo_task = input("Enter a task: ") + "\n"

            # file = open('todos.txt', 'r')
            # todo_list = file.readlines()
            # file.close()

            with open('todos.txt', 'r') as file:
                todo_list = file.readlines()

            todo_list.append(todo_task)

            with open('todos.txt', 'w') as file:
                file.writelines(todo_list)

        case "show" | "display":
            with open('todos.txt', 'r') as file:
                todo_list = file.readlines()

            # for item in todo_list:
            #     index = todo_list.index(item)
            #     item = item.strip('\n')
            #     todo_list[index] = item

            # List comprehension
            todo_list = [item.strip('\n') for item in todo_list]

            display_to_do_list(todo_list)
        case "edit":
            with open('todos.txt', 'r') as file:
                todo_list = file.readlines()

            display_to_do_list(todo_list)
            edit_input = int(input("Enter the position of the item you want to edit: ")) - index_updater
            todo_list[edit_input] = input("Enter new task") + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todo_list)
        case "complete":
            with open('todos.txt', 'r') as file:
                todo_list = file.readlines()

            display_to_do_list(todo_list)
            complete_input = int(input("Enter the position of the item you want to complete: ")) - index_updater
            todo_list.pop(complete_input)

            with open('todos.txt', 'w') as file:
                file.writelines(todo_list)
        case "exit":
            break
        case _:
            print("You entered an invalid command")
