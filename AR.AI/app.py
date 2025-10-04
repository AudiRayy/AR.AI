import streamlit as st
from PyPDF2 import PdfReader
import openai

# Page config
st.set_page_config(page_title="AR.AI", page_icon="🤖", layout="centered")

st.title("Welcome to AR.AI")
st.write("Your AI app for summarizing PDFs and text!")

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
if uploaded_file:
    reader = PdfReader(uploaded_file)
    text = "".join([page.extract_text() for page in reader.pages if page.extract_text()])
    st.write("**PDF Content Preview:**")
    st.write(text[:1000], "...")  # preview first 1000 characters

    # AI Summarize (example, using OpenAI API key)
    api_key = st.text_input("Enter your OpenAI API Key", type="password")
    if api_key and st.button("Summarize PDF"):
        openai.api_key = api_key
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Summarize the following text:\n{text}",
            temperature=0.5,
            max_tokens=300
        )
        summary = response.choices[0].text.strip()
        st.write("**Summary:**")
        st.write(summary)