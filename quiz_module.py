from gemini_client import generate

def generate_quiz(topic: str, number_of_questions: int = 5) -> str:
    number_of_questions = max(1, min(number_of_questions, 20))

    prompt = f"""
You are EduGenie, an educational quiz generator.

Create {number_of_questions} multiple-choice questions about:
{topic}

For every question provide:
A. option
B. option
C. option
D. option

At the end provide an Answer Key in this format:
1. B
2. A
etc.

Do not give the answer immediately after each question.
"""
    return generate(prompt)
