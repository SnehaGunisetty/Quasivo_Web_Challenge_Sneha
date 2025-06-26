import streamlit as st
from utils import generate_questions

st.set_page_config(page_title="Step 3 – Generate Interview Questions", layout="centered")
st.title("Step 3: Generate Interview Questions")

# Load JD and Résumé from session
jd = st.session_state.get('jd_text', '')
resume = st.session_state.get('resume_text', '')

# Ensure both are available
if not jd or not resume:
    st.error("Missing JD or Resume. Please go back to Step 2 and enter both.")
    st.stop()

# Generate Questions
if st.button("Generate Questions with Gemini"):
    with st.spinner("Talking to Gemini..."):
        questions = generate_questions(jd, resume)
        st.session_state['questions'] = questions

# Display Questions
if 'questions' in st.session_state:
    st.success("Questions generated successfully!")
    st.subheader("Generated Interview Questions:")

    for i, q in enumerate(st.session_state['questions'], 1):
        st.markdown(f"**Q{i}.** {q}")

    # Button to proceed
    st.markdown("---")
    if st.button("Proceed to Answer Questions"):
        st.switch_page("pages/4_collect_answers.py")  # Will create in next step
