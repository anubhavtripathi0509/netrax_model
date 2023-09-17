import pickle
from pathlib import Path


import streamlit as st
from PIL import Image
import helper



# Logo
image = Image.open('Logo1.png')
st.image(image)

st.sidebar.title(f"Welcome at M1")
st.sidebar.subheader("This is an model for Diabetic retinopathy")
# Upload
uploaded_file = st.sidebar.file_uploader("Upload your file here...", type=['png', 'jpeg', 'jpg'])
if uploaded_file is not None:
    st.image(uploaded_file)

    if st.sidebar.button("Show Result"):
        predicted_output = helper.Diabetic_Retinopathy(uploaded_file)
        st.header("Result")
        st.text(f"Predicted Output: {predicted_output}")