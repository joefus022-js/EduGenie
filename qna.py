from gemini_client import generate

def answer_question(question: str) -> str:
    prompt = f"""
You are EduGenie, a friendly educational assistant.

Answer the student's question accurately and clearly.
Keep the explanation concise but useful.
Use examples when they help.

Student question:
{question}
"""
    return generate(prompt)
