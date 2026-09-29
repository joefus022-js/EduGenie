from gemini_client import generate

def summarize_text(text: str) -> str:
    prompt = f"""
You are EduGenie.

Summarize the following educational text.

Requirements:
- Give a short overview.
- List the main points.
- Keep important facts.
- Use simple student-friendly language.
- Do not add information that is not in the text.

Educational text:
{text}
"""
    return generate(prompt)
