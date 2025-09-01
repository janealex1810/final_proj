import pytest
import allure
import requests
from config import settings, test_data

headers = {"X-API-KEY": test_data.API_TOKEN}

@pytest.mark.api
@allure.feature("API Tests")
class TestAPI:
    @allure.step("Поиск фильма по API")
    def test_search_movie_api(self):
        r = requests.get(f"{settings.API_URL}/movie", params={"name": "Интерстеллар"}, headers=headers)
        assert r.status_code == 200
        assert "docs" in r.json()

    @allure.step("Получение информации о фильме")
    def test_get_movie_info(self):
        r = requests.get(f"{settings.API_URL}/movie/301", headers=headers)
        assert r.status_code == 200
        assert r.json().get("name") == "Интерстеллар"

    @allure.step("Список топ-250")
    def test_top_movies(self):
        r = requests.get(f"{settings.API_URL}/movie", params={"top250": "!null"}, headers=headers)
        assert r.status_code == 200

    @allure.step("Фильтрация по жанру")
    def test_filter_genre(self):
        r = requests.get(f"{settings.API_URL}/movie", params={"genres.name": "комедия"}, headers=headers)
        assert r.status_code == 200

    @allure.step("Некорректный запрос")
    def test_invalid_request(self):
        r = requests.get(f"{settings.API_URL}/invalid", headers=headers)
        assert r.status_code in [400, 404]
