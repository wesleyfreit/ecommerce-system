from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
