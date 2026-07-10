import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Smart To-Do", layout="wide")

st.title("📝 Smart To-Do App")

# Initialize session state
if 'tasks' not in st.session_state:
    if os.path.exists('tasks.csv'):
        st.session_state.tasks = pd.read_csv('tasks.csv')
    else:
        st.session_state.tasks = pd.DataFrame(columns=['Task', 'Priority', 'Category', 'Done'])

# Add new task
col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    new_task = st.text_input("Add a new task")
with col2:
    priority = st.selectbox("Priority", ["Low", "Medium", "High"])
with col3:
    category = st.text_input("Category", value="General")

if new_task:
    new_row = pd.DataFrame({'Task': [new_task], 'Priority': [priority], 'Category': [category], 'Done': [False]})
    st.session_state.tasks = pd.concat([st.session_state.tasks, new_row], ignore_index=True)
    st.session_state.tasks.to_csv('tasks.csv', index=False)
    st.rerun()

# Display tasks
st.subheader("Your Tasks")
if not st.session_state.tasks.empty:
    st.dataframe(st.session_state.tasks, use_container_width=True)
else:
    st.info("No tasks yet. Add one to get started!")
