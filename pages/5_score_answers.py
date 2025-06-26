import streamlit as st
from utils import score_answer

st.set_page_config(page_title="Step 5 – Score Answers", layout="centered")
st.title("Step 5: Scoring Candidate Answers")

questions = st.session_state.get('questions', [])
answers = st.session_state.get('answers', [])

if not questions or not answers:
    st.error("Missing questions or answers. Please complete previous steps.")
    st.stop()

# Run scoring
if st.button("Score Answers with Gemini"):
    st.session_state['scores'] = []
    st.session_state['reasons'] = []
    with st.spinner("Scoring in progress..."):
        for q, a in zip(questions, answers):
            score, reason = score_answer(q, a)
            st.session_state['scores'].append(score)
            st.session_state['reasons'].append(reason)

# Display results
if 'scores' in st.session_state:
    st.success("Answers scored successfully!")
    st.subheader("Results:")

    for i, (q, a, s, r) in enumerate(zip(questions, answers, st.session_state['scores'], st.session_state['reasons'])):
        st.markdown(f"### Question {i+1}")
        st.markdown(f"**Q:** {q}")
        st.markdown(f"**A:** {a}")
        st.markdown(f"**Score:** {s} / 10")
        st.markdown(f"**Reason:** {r}")
        st.markdown("---")

    if st.button("Save and Show Summary"):
        st.switch_page("pages/6_summary_save.py")  # Final step
