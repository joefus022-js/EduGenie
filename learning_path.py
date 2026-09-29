from gemini_client import generate

def create_learning_path(subject: str, level: str = "Beginner", weeks: int = 6) -> str:
    weeks = max(1, min(52, weeks))

    prompt = f"""
You are EduGenie, a personalized learning planner.

Create a structured learning path for:
Subject: {subject}
Current level: {level}
Duration: {weeks} weeks

Include:
1. Learning goal
2. Week-by-week topics
3. Beginner to advanced progression
4. Practice activities
5. Mini-project ideas
6. Free-resource suggestions by resource type
7. Final revision/checkpoint

Make it realistic for a college student.
"""
    return generate(prompt)
