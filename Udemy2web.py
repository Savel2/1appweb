import streamlit as st
from Udemy2Functions import get_todos, write_todos


todos = get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
 # session_state is kind of dictionary sintax. Somehow it work with input on the 19th line. Prob because of new todo key
    todos.append(todo)
    write_todos(todos)

st.title("Yoyo wasup. This is the main title")
st.subheader("This is subheader")
st.write("This is simple text") #this is for the simple text



for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key= todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo] #in order to delete complete todo from st.session
        st.experimental_rerun() #to rerun the code (this is neede for checkboxes)

st.text_input(label = "", placeholder= "Enter new todo...",
               on_change = add_todo, key = "new_todo") #label arguement is required, that's why I left it in parentheses. The on_change event occurs when the value of an HTML element is changed.