import streamlit as st
import functions


def addtodo():
    todo = st.session_state["new_todo"]+'\n'
    todos.append(todo)
    functions.write_todos(todos)
    print(todo)


todos = functions.get_todos()
st.title("my todo app")
st.subheader('this app is to manage the daily tasks')
st.subheader('this app is to manage the daily tasks')


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="add new todo", placeholder="add todo",
              on_change=addtodo, key="new_todo")

st.session_state
