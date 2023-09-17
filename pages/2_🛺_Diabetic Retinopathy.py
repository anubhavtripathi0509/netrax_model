import streamlit as st
import helper

st.title("Diabetic Retinopathy Detection")
# st.sidebar.subheader("This is an model for Diabetic retinopathy")
# Upload
uploaded_file = st.sidebar.file_uploader("Upload your file here...", type=['png', 'jpeg', 'jpg'])
if uploaded_file is not None:
    st.image(uploaded_file)

    if st.sidebar.button("Show Result"):
        predicted_output = helper.Diabetic_Retinopathy(uploaded_file)
        st.header("Result")
        st.text(f"Predicted Output: {predicted_output}")