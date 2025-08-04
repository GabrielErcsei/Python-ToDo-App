from modules import functions
import FreeSimpleGUI as simpleGui


label = simpleGui.Text("Type in a to-do item")
input_box = simpleGui.InputText(tooltip="Enter to-do")
add_button = simpleGui.Button(button_text="Add")

window = simpleGui.Window("My To-Do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()