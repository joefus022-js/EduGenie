# EduGenie - Google Gemini Powered Learning Assistant

EduGenie is a student-focused AI learning assistant built with FastAPI,
HTML/CSS/JavaScript, and the Google Gemini API.

## Features

- Ask educational questions
- Explain difficult concepts simply
- Generate multiple-choice quizzes
- Summarize educational text
- Create personalized learning paths

## Project Structure

```text
EduGenie/
├── main.py
├── gemini_client.py
├── qna.py
├── explanation_module.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Setup

### 1. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install packages

```bash
pip install -r requirements.txt
```

### 3. Create `.env`

Copy `.env.example` to `.env` and add your Gemini API key:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Do not upload `.env` to GitHub.

### 4. Start the server

```bash
uvicorn main:app --reload
```

### 5. Open the website

Open:

```text
http://127.0.0.1:8000
```

The frontend is served directly by FastAPI, so you do not need Live Server.

## API Endpoints

- POST `/qa`
- POST `/explain`
- POST `/quiz`
- POST `/summarize`
- POST `/learn/recommendations`
- GET `/health`
