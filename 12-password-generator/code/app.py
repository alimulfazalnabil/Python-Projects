import streamlit as st
import string
import random

st.set_page_config(page_title="Password Generator", layout="centered")
st.title("🔐 Password Generator")

# Settings
col1, col2 = st.columns(2)
with col1:
    length = st.slider("Password Length", min_value=8, max_value=32, value=12)
with col2:
    count = st.slider("Generate Passwords", min_value=1, max_value=5, value=1)

# Character options
col1, col2, col3, col4 = st.columns(4)
with col1:
    use_upper = st.checkbox("Uppercase", value=True)
with col2:
    use_lower = st.checkbox("Lowercase", value=True)
with col3:
    use_digits = st.checkbox("Digits", value=True)
with col4:
    use_special = st.checkbox("Special", value=True)

# Generate button
if st.button("Generate Passwords"):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if characters:
        for i in range(count):
            password = ''.join(random.choice(characters) for _ in range(length))
            st.code(password, language="text")
    else:
        st.error("Select at least one character type!")
