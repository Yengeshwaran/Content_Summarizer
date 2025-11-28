import streamlit as st
import summarization_lib as glib

st.set_page_config(page_title="Content Summarizer", layout="wide")
st.title("Content Summarizer")

# Create two columns
left_col, right_col = st.columns([1, 1])

with left_col:
    input_text = st.text_area("How would you like the document summarized?")

    uploaded_file = st.file_uploader("Upload your PDF file", type=["pdf"])

    summarize_button = st.button("Summarize", type="primary")

with right_col:
    st.subheader("Summary Output")

    if summarize_button:
        if uploaded_file is None:
            st.error("Please upload a PDF file before summarizing.")
        elif not input_text.strip():
            st.error("Please enter how you want the document summarized.")
        else:
            with st.spinner("Running..."):
                response_content = glib.get_summary(input_text, uploaded_file)
                st.write(response_content)
