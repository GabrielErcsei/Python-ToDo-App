import streamlit as st
from modules import functions


todo_list = functions.get_todos_from_file()

def add_todo():
    todo_item = st.session_state["todo_input"] + "\n"
    todo_list.append(todo_item)
    functions.write_todos_to_file(todo_item)


st.title("Todo app")
st.write("This app allows for increased productivity.")


for todo in todo_list:
    st.checkbox(todo)

st.text_input(label="", placeholder="Type in a todo", on_change=add_todo, key="todo_input")

st.session_state