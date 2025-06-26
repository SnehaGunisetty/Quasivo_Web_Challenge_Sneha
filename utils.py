from dotenv import load_dotenv
import os
import requests

# Load API Key from .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Gemini API URL
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

def generate_questions(jd, resume):
    prompt = f"""
You are an AI HR assistant. Given the following job description and candidate resume, generate 3 custom interview questions that test the candidate’s fit for the role.

Job Description:
{jd}

Candidate Résumé:
{resume}

Only return the 3 questions in a numbered list.
"""

    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(GEMINI_URL, headers=headers, json=payload)
    result = response.json()

    try:
        text_output = result["candidates"][0]["content"]["parts"][0]["text"]
        lines = text_output.strip().splitlines()
        
        # Only keep lines that look like questions
        questions = [line.strip("1234567890. ").strip() for line in lines if "?" in line]
        return questions
    except Exception as e:
        return [f"Error: {str(e)}"]

def score_answer(question, answer):
    prompt = f"""
You are an AI interviewer. Given a question and the candidate's answer, score it from 1 to 10 and explain your rating.

Question: {question}
Answer: {answer}

Format:
Score: X
Reason: <short explanation>
"""
    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(GEMINI_URL, headers=headers, json=payload)
    result = response.json()

    try:
        text_output = result["candidates"][0]["content"]["parts"][0]["text"]
        # Extract score and reason from response
        lines = text_output.strip().splitlines()
        score_line = next((l for l in lines if "Score:" in l), None)
        reason_line = next((l for l in lines if "Reason:" in l), "Reason: Not provided.")
        score = int(score_line.split(":")[1].strip()) if score_line else 0
        reason = reason_line.split(":", 1)[1].strip()
        return score, reason
    except Exception as e:
        return 0, f"Error: {str(e)}"
