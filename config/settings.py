import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://www.kinopoisk.ru")
API_URL = os.getenv("API_URL", "https://api.kinopoisk.dev")
