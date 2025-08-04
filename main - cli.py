# from modules.functions import get_todos_from_file, write_todos_to_file, display_to_do_list, index_updater
from modules import functions as lecture_one_functions
import time
import datetime

todo_list = []

current_time = time.strftime("%b-%d-%Y, %H:%M:%S")
print(current_time)
while True:
    user_input_action = input("Type add, show, edit, complete or exit to interact withe the to do list: ").strip()

    if user_input_action.startswith("add"):
        # list slicing
        todo_task = user_input_action[4:]

        todo_list = lecture_one_functions.get_todos_from_file()

        todo_list.append(todo_task + '\n')

        lecture_one_functions.write_todos_to_file(todos=todo_list)

    elif user_input_action.startswith("show"):
        todo_list = lecture_one_functions.get_todos_from_file()

        # for item in todo_list:
        #     index = todo_list.index(item)
        #     item = item.strip('\n')
        #     todo_list[index] = item

        # List comprehension
        todo_list = [item.strip('\n') for item in todo_list]

        lecture_one_functions.display_to_do_list(todo_list)
    elif user_input_action.startswith("edit"):
        try:
            todo_list = lecture_one_functions.get_todos_from_file()

            lecture_one_functions.display_to_do_list(todo_list)
            # edit_input = int(input("Enter the position of the item you want to edit: ")) - index_updater
            edit_input = int(user_input_action[5:]) - lecture_one_functions.INDEX
            todo_list[edit_input] = input("Enter new task") + '\n'

            lecture_one_functions.write_todos_to_file(todos=todo_list)

        except ValueError:
            print("You entered a wrong command")
            # continues the while loop
            continue

    elif user_input_action.startswith("complete"):
        try:
            todo_list = lecture_one_functions.get_todos_from_file()

            lecture_one_functions.display_to_do_list(todo_list)
            # complete_input = int(input("Enter the position of the item you want to complete: ")) - index_updater
            complete_input = int(user_input_action[9:]) - lecture_one_functions.INDEX

            todo_list.pop(complete_input)

            lecture_one_functions.write_todos_to_file(todos=todo_list)

        except ValueError:
            print("You entered a wrong command")
            # continues the while loop - makes the code go back to the beginning of the loop
            continue

    elif user_input_action.startswith("exit"):
        break

    else:
        print("Invalid command")