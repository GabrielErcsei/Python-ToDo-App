import time

from modules import functions
import FreeSimpleGUI as simpleGui
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

simpleGui.theme('Black')
system_clock = simpleGui.Text("", key="system_clock")
label = simpleGui.Text("Type in a to-do item")
input_box = simpleGui.InputText(tooltip="Enter to-do", key="todo")
add_button = simpleGui.Button(key="add_button", image_source='images/add.png', size=2,
                              mouseover_colors='LightBlue2', tooltip='Add')
list_box = simpleGui.Listbox(values=functions.get_todos_from_file(), key="todo_items",
                             enable_events=True, size=(45, 10))
edit_button = simpleGui.Button(button_text="Edit", key="edit_button")
complete_button = simpleGui.Button(button_text="Complete Task", key="complete_button")
exit_button = simpleGui.Button(button_text="Exit", key="exit_button")

window = simpleGui.Window("My To-Do App",
                          layout=[[system_clock],
                                  [label], [input_box, add_button],
                                  [list_box, edit_button, complete_button],
                                  [exit_button]],
                          font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=200)
    window['system_clock'].update(value=time.strftime("%b %d %Y %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case 'add_button':
            todo_list = functions.get_todos_from_file()
            todo_list.append(values['todo'] + '\n')
            functions.write_todos_to_file(todo_list)
            window['todo_items'].update(values=todo_list)

        case 'edit_button':
            try:
                item_to_edit = values['todo_items'][0]
                new_todo = values['todo']

                todo_list = functions.get_todos_from_file()
                item_to_edit_index = todo_list.index(item_to_edit)
                todo_list[item_to_edit_index] = new_todo
                functions.write_todos_to_file(todo_list)
                window['todo_items'].update(values=todo_list)
            except IndexError:
                simpleGui.popup("Please select a todo item", font=('Helvetica', 20))
        case 'complete_button':
            try:
                item_to_complete = values['todo_items'][0]
                todo_list = functions.get_todos_from_file()
                todo_list.remove(item_to_complete)
                functions.write_todos_to_file(todo_list)
                window['todo_items'].update(values=todo_list)
                window['todo'].update(value='')
            except IndexError:
                simpleGui.popup("Please select a todo item", font=('Helvetica', 20))

        case 'exit_button':
            break
        case "todo_items":
                window['todo'].update(value=values['todo_items'][0])
        case simpleGui.WINDOW_CLOSED:
            break


window.close()


