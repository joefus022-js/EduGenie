import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# Find .env in the EduGenie project folder
BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / ".env"

# Load the .env file
load_dotenv(dotenv_path=ENV_FILE, override=True)

# Models to try in order
MODEL_NAMES = [
    "gemini-3.8-flash",
    "gemini-3.7-flash",
    "gemini-3.6-flash",
    "gemini-3.5-flash-lite"
]

# Get API key
_api_key = os.getenv("GEMINI_API_KEY")

if not _api_key:
    raise RuntimeError(
        f"GEMINI_API_KEY not found.\n"
        f"Expected .env file at: {ENV_FILE}"
    )

_api_key = _api_key.strip()

print("Gemini API key loaded successfully.")

# Create Gemini client
client = genai.Client(api_key=_api_key)

# MODEL_NAME = "gemini-3.6-flash"


# def generate(prompt: str) -> str:
#     response = client.models.generate_content(
#         model=MODEL_NAME,
#         contents=prompt
#     )

#     return response.text or "No response returned."

def generate(prompt: str) -> str:
    last_error = None

    for model_name in MODEL_NAMES:
        try:
            print(f"Trying Gemini model: {model_name}")

            response = client.models.generate_content(
                model=model_name,
                contents=prompt
            )

            print(f"Success with: {model_name}")
            return response.text or "No response returned."

        except Exception as error:
            last_error = error
            print(f"{model_name} unavailable. Trying next model...")

    raise RuntimeError(
        f"All Gemini models are currently unavailable. Last error: {last_error}"
    )