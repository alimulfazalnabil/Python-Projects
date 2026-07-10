import streamlit as st
import markdown

st.set_page_config(page_title="Markdown Previewer", layout="wide")
st.title("📝 Markdown Previewer")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Markdown Input")
    markdown_text = st.text_area("Enter your markdown here:", height=400, value="# Hello\n\nThis is **bold** text.")

with col2:
    st.subheader("Preview")
    html_content = markdown.markdown(markdown_text)
    st.markdown(markdown_text)

# Export options
st.divider()
if st.button("📥 Export as HTML"):
    st.download_button(
        label="Download HTML",
        data=html_content,
        file_name="preview.html",
        mime="text/html"
    )
