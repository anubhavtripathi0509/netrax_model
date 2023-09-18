import streamlit as st
import helper

st.set_page_config(
    page_title="NetraX Healthcare",
    page_icon="🔥",
)

st.title("Diabetic Retinopathy Detection")
# st.sidebar.subheader("This is an model for Diabetic retinopathy")
# Upload
uploaded_file = st.sidebar.file_uploader("Upload your file here...", type=['png', 'jpeg', 'jpg'])
if uploaded_file is not None:
    st.image(uploaded_file)

    if st.sidebar.button("Show Result"):
        predicted_output = helper.Diabetic_Retinopathy(uploaded_file)
        glaucoma_output = helper.Glaucoma_Detection(uploaded_file)
        st.header("Result")
        st.subheader(f"Predicted Output of Diabetic Retinopathy: {predicted_output}")
        st.subheader(f"Predicted Output of Glaucoma: {glaucoma_output}")