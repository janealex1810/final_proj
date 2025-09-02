import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://www.kinopoisk.ru")
BASE_URL_CINEMA = os.getenv("BASE_URL_CINEMA", "https://www.kinopoisk.ru/lists/movies/movies-in-cinema/")
BASE_URL_MEDIA = os.getenv("BASE_URL_MEDIA", "https://www.kinopoisk.ru/media/")
API_URL = os.getenv("API_URL", "https://api.kinopoisk.dev/v1.4")
