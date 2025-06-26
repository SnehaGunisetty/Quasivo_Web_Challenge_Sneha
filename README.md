# Quasivo_Web_Challenge_Sneha - Candidate Screening Web App


This is a locally-hosted AI-powered web app that automates first-round candidate screening using the Google Gemini API.

---

## Features

- Upload or paste Job Descriptions and Resumes
- Uses Gemini AI to:
  - Compare Resume vs. Job Description
  - Generate 3 custom interview questions
  - Collect candidate answers
  - Score each answer (1–10 scale)
- Display summary results
- Save each session locally as .json file

---

## Requirements

- Python 3.11 (recommended)
- Local environment (no cloud deployment)
- pip (Python package manager)

---

## Setup Instructions

### 1. Clone or Download the Repository

```bash
git clone https://github.com/SnehaGunisetty/Quasivo_Web_Challenge_Sneha.git
cd Quasivo_Web_Challenge_Sneha
```

### 2. Check Python Version

Make sure Python 3.11 is installed:

```bash
python --version
pip --version
```

If your Python version is below 3.11, download and install from:

https://www.python.org/downloads/release/python-3110/

### 3. Install Dependencies

After Python 3.11 is installed, run:

```bash
py -3.11 -m pip install -r requirements.txt
```

(Ensure you're using the correct Python version if multiple are installed.)

### 4. Run the Application

If you're using Python 3.11:

```bash
python -m streamlit run app.py
```

Or with the explicit version:

```bash
py -3.11 -m streamlit run app.py
```

---

## Notes

- You’ll need a Gemini API key in a .env file like this:

  ```
  GEMINI_API_KEY=your_actual_key_here
  ```

- Results are saved inside the /data folder.

- Tested with Streamlit ≥ 1.31 and Python 3.11.8.
