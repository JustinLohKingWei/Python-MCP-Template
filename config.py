import os
from dotenv import load_dotenv
from config import DEBUG, APP_NAME


load_dotenv()

# App
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
APP_NAME = os.getenv("APP_NAME", "AI Agent Integration Hub")

# Add integration credentials here
# SOME_CLIENT_ID = os.getenv("SOME_CLIENT_ID")
# SOME_CLIENT_SECRET = os.getenv("SOME_CLIENT_SECRET")