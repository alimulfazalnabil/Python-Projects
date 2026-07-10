import streamlit as st
import random

st.set_page_config(page_title="Quiz Game", layout="wide")
st.title("🎯 Quiz Game")

questions = [
    {"q": "What is 2+2?", "options": ["3", "4", "5", "6"], "answer": "4"},
    {"q": "What is the capital of France?", "options": ["London", "Berlin", "Paris", "Madrid"], "answer": "Paris"},
    {"q": "What is the largest planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Jupiter"},
]

if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.current_question = 0

if st.session_state.current_question < len(questions):
    q = questions[st.session_state.current_question]
    st.subheader(f"Question {st.session_state.current_question + 1}/{len(questions)}")
    st.write(q["q"])
    
    answer = st.radio("Choose an answer:", q["options"], key=f"q{st.session_state.current_question}")
    
    if st.button("Submit"):
        if answer == q["answer"]:
            st.session_state.score += 1
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Wrong! The correct answer is {q['answer']}")
        
        st.session_state.current_question += 1
        st.rerun()
else:
    st.subheader(f"Quiz Complete! 🎉")
    st.metric("Your Score", f"{st.session_state.score}/{len(questions)}")
    if st.button("Restart Quiz"):
        st.session_state.score = 0
        st.session_state.current_question = 0
        st.rerun()
