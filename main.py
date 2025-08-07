from modules import functions
import FreeSimpleGUI as simpleGui


label = simpleGui.Text("Type in a to-do item")
input_box = simpleGui.InputText(tooltip="Enter to-do", key="todo")
add_button = simpleGui.Button(button_text="Add", key="add_button")

window = simpleGui.Window("My To-Do App",
                          layout=[[label], [input_box, add_button]],
                          font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'add_button':
            todo_list = functions.get_todos_from_file()
            todo_list.append(values['todo'] + '\n')
            functions.write_todos_to_file(todo_list)
        case simpleGui.WIN_CLOSED:
            break


window.close()


