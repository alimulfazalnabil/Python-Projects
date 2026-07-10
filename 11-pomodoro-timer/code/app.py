import streamlit as st
import time

st.set_page_config(page_title="Pomodoro Timer", layout="centered")
st.title("⏱️ Pomodoro Timer")

# Settings
col1, col2 = st.columns(2)
with col1:
    work_duration = st.number_input("Work Duration (minutes)", value=25, min_value=1)
with col2:
    break_duration = st.number_input("Break Duration (minutes)", value=5, min_value=1)

# Initialize session state
if "session_started" not in st.session_state:
    st.session_state.session_started = False
    st.session_state.session_count = 0

# Start/Stop button
if st.button("▶️ Start Timer"):
    st.session_state.session_started = True

if st.session_state.session_started:
    # Work session
    placeholder = st.empty()
    work_seconds = work_duration * 60
    
    for i in range(work_seconds, 0, -1):
        with placeholder.container():
            mins, secs = divmod(i, 60)
            st.metric("Work Time", f"{mins:02d}:{secs:02d}")
            time.sleep(1)
    
    st.success("Work session complete! Time for a break.")
    st.session_state.session_count += 1
    
    # Break session
    break_seconds = break_duration * 60
    for i in range(break_seconds, 0, -1):
        with placeholder.container():
            mins, secs = divmod(i, 60)
            st.metric("Break Time", f"{mins:02d}:{secs:02d}")
            time.sleep(1)
    
    st.info("Break complete!")
    st.session_state.session_started = False

st.metric("Sessions Completed", st.session_state.session_count)
