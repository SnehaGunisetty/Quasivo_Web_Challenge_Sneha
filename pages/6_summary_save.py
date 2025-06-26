import streamlit as st
import uuid
import json
import os

st.set_page_config(page_title="Step 6 – Summary & Save", layout="centered")
st.title("Final Summary & Save")

# Load all data from session
jd = st.session_state.get('jd_text', '')
resume = st.session_state.get('resume_text', '')
questions = st.session_state.get('questions', [])
answers = st.session_state.get('answers', [])
scores = st.session_state.get('scores', [])
reasons = st.session_state.get('reasons', [])

# Ensure everything exists
if not (jd and resume and questions and answers and scores):
    st.error("Missing information. Please complete previous steps.")
    st.stop()

st.subheader("Job Description")
st.code(jd, language='markdown')

st.subheader("Candidate Resume")
st.code(resume, language='markdown')

for i, (q, a, s, r) in enumerate(zip(questions, answers, scores, reasons)):
    st.markdown(f"### Question {i+1}")
    st.markdown(f"**Q:** {q}")
    st.markdown(f"**A:** {a}")
    st.markdown(f"**Score:** {s} / 10")
    st.markdown(f"**Reason:** {r}")
    st.markdown("---")

# Save data to JSON
if st.button("Save Results to File"):
    record = {
        "job_description": jd,
        "resume": resume,
        "questions": questions,
        "answers": answers,
        "scores": scores,
        "reasons": reasons
    }

    filename = f"data/{uuid.uuid4()}.json"

    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(record, f, indent=2)

    st.success(f"Results saved to `{filename}`")
