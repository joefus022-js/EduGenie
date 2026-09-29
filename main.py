from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import create_learning_path

app = FastAPI(
    title="EduGenie - Google Gemini Powered Learning Assistant"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TextRequest(BaseModel):
    text: str


class QuizRequest(BaseModel):
    topic: str
    number_of_questions: int = 5


class LearningRequest(BaseModel):
    subject: str
    level: str = "Beginner"
    weeks: int = 6


@app.get("/health")
def health():
    return {"status": "EduGenie is running"}


@app.post("/qa")
def qa(request: TextRequest):
    return {
        "answer": answer_question(request.text)
    }


@app.post("/explain")
def explain(request: TextRequest):
    return {
        "answer": explain_topic(request.text)
    }


@app.post("/quiz")
def quiz(request: QuizRequest):
    return {
        "answer": generate_quiz(
            request.topic,
            request.number_of_questions
        )
    }


@app.post("/summarize")
def summarize(request: TextRequest):
    return {
        "answer": summarize_text(request.text)
    }


@app.post("/learn/recommendations")
def learning_path(request: LearningRequest):
    return {
        "answer": create_learning_path(
            request.subject,
            request.level,
            request.weeks
        )
    }


app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


@app.get("/")
def home():
    return FileResponse("templates/index.html")