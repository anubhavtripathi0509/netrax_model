import pickle
from pathlib import Path


import streamlit as st
from PIL import Image
import helper

st.set_page_config(
    page_title="NetraX Healthcare",
    page_icon="🔥",
)

# Logo
image = Image.open('Logo1.png')
st.image(image)


# st.sidebar.title(f"Welcome to NetraX")
st.sidebar.success("Select a page above")