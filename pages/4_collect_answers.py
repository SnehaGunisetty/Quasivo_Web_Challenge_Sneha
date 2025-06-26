import streamlit as st

st.set_page_config(page_title="Step 4 – Candidate Answers", layout="centered")
st.title("Step 4: Answer Interview Questions")

questions = st.session_state.get('questions', [])

if not questions:
    st.error("No questions found. Please go back to Step 3 and generate them.")
    st.stop()

st.subheader("Please answer the following questions:")

# Store answers in session_state if not already there
if 'answers' not in st.session_state:
    st.session_state['answers'] = ['' for _ in questions]

# Input fields for each answer
for i, question in enumerate(questions):
    st.markdown(f"**Q{i+1}. {question}**")
    st.session_state['answers'][i] = st.text_area(
        f"Your Answer to Q{i+1}",
        value=st.session_state['answers'][i],
        key=f"answer_{i}",
        height=100
    )

# Proceed Button
if st.button("Submit Answers and Continue to Scoring"):
    st.success("Answers submitted successfully!")
    st.switch_page("pages/5_score_answers.py")  # Step 5
