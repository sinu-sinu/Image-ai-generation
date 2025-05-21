import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")
SERVICE_ACCOUNT_PATH = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON")
IMGUR_CLIENT_ID = os.getenv("IMGUR_CLIENT_ID")

if not IMGUR_CLIENT_ID:
    raise ValueError("Missing Imgur Client ID in .env")

if not HF_API_KEY:
    raise ValueError("Missing Hugging Face api Key in .env")

if not SERVICE_ACCOUNT_PATH:
    raise ValueError("Missing Google Service Account path in .env")
