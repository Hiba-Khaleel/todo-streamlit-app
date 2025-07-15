import streamlit as st
import functions

todos = functions.get_todos(filepath="todos.txt")
st.title("my todo app")
st.subheader('this app is to manage the daily tasks')
st.subheader('this app is to manage the daily tasks')


for todo in todos:
    st.checkbox(todo)

st.text_input(label="add new todo", placeholder="add todo")
