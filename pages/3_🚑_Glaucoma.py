import streamlit as st
import helper

st.title("Glaucoma Detection")
# st.sidebar.subheader("This is an model for Diabetic retinopathy")
# Upload
uploaded_file = st.sidebar.file_uploader("Upload your file here...", type=['png', 'jpeg', 'jpg'])
if uploaded_file is not None:
    st.image(uploaded_file)

    if st.sidebar.button("Show Result"):
        glaucoma_output = helper.Glaucoma_Detection(uploaded_file)
        st.header("Result")
        st.text(f"Predicted Output: {glaucoma_output}")