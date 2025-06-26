import streamlit as st
import fitz  # PyMuPDF

st.set_page_config(page_title="Quasivo AI Screening", layout="centered")

st.title("Quasivo AI Challenge – Input Collection")

st.subheader("Step 1: Upload Job Description")
jd_text = st.text_area("Paste the job description here", height=200)
jd_file = st.file_uploader("Or upload a JD file (.txt)", type=["txt"])

if jd_file is not None and not jd_text:
    jd_text = jd_file.read().decode("utf-8")

st.markdown("---")

st.subheader("Step 2: Upload Candidate Resume")
resume_text = st.text_area("Paste the resume here", height=200)
resume_file = st.file_uploader("Or upload a resume (.pdf)", type=["pdf"])

if resume_file is not None and not resume_text:
    with fitz.open(stream=resume_file.read(), filetype="pdf") as doc:
        resume_text = ""
        for page in doc:
            resume_text += page.get_text()

st.markdown("---")

# Display preview if both inputs are collected
if jd_text and resume_text:
    st.success("Inputs received!")
    if st.button("Proceed to Next Step"):
        st.session_state['jd_text'] = jd_text
        st.session_state['resume_text'] = resume_text
        st.switch_page("pages/3_generate_questions.py")  # Placeholder for next step

else:
    st.info("Please enter or upload both JD and resume to continue.")
