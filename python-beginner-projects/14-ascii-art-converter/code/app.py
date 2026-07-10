import streamlit as st
from PIL import Image
import io

st.set_page_config(page_title="ASCII Art Converter", layout="wide")
st.title("🎨 ASCII Art Converter")

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ","]

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(image, caption="Original Image", use_column_width=True)
    
    with col2:
        width = st.slider("ASCII Width", min_value=20, max_value=150, value=80)
    
    # Convert to ASCII
    aspect_ratio = image.height / image.width
    height = int(width * aspect_ratio * 0.5)
    
    image = image.resize((width, height))
    pixels = image.convert("L").getdata()
    
    ascii_art = ""
    for pixel in pixels:
        ascii_art += ASCII_CHARS[pixel // 25]
    
    ascii_str = ""
    for i in range(0, len(ascii_art), width):
        ascii_str += ascii_art[i:i+width] + "\n"
    
    with col2:
        st.subheader("ASCII Art")
        st.code(ascii_str, language="text")
    
    # Download
    st.download_button(
        label="Download ASCII Art",
        data=ascii_str,
        file_name="ascii_art.txt",
        mime="text/plain"
    )
