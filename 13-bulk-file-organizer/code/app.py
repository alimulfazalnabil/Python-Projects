import streamlit as st
import os
import shutil
from pathlib import Path

st.set_page_config(page_title="File Organizer", layout="wide")
st.title("📁 Bulk File Organizer")

# Directory selection
directory = st.text_input("Enter directory path", value=str(Path.home() / "Downloads"))

if st.button("Scan Directory"):
    if os.path.exists(directory):
        files = os.listdir(directory)
        
        st.subheader(f"Files in {directory}")
        st.info(f"Total files: {len(files)}")
        
        # Group by extension
        extensions = {}
        for file in files:
            if os.path.isfile(os.path.join(directory, file)):
                ext = Path(file).suffix or "No Extension"
                extensions[ext] = extensions.get(ext, 0) + 1
        
        st.write("Files by type:")
        for ext, count in sorted(extensions.items()):
            st.write(f"- {ext}: {count} files")
        
        # Organize button
        if st.button("Organize by Type"):
            for file in files:
                file_path = os.path.join(directory, file)
                if os.path.isfile(file_path):
                    ext = Path(file).suffix[1:] or "No Extension"
                    folder = os.path.join(directory, ext)
                    os.makedirs(folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(folder, file))
            st.success("Files organized!")
    else:
        st.error("Directory not found")
