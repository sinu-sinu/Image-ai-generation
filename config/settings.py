import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERVICE_ACCOUNT_PATH = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON")

if not OPENAI_API_KEY:
    raise ValueError("Missing OpenAI API Key in .env")

if not SERVICE_ACCOUNT_PATH:
    raise ValueError("Missing Google Service Account path in .env")
