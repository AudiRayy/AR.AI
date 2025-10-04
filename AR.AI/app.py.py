import streamlit as st

st.title("AR.AI")
st.write("Welcome to AR.AI")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
if uploaded_file is not None:
    st.success("File uploaded successfully!")

