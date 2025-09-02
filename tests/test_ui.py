import pytest
import allure
from config import settings
from pages.search_page import SearchPage


@pytest.mark.ui
@allure.feature("UI Tests")
class TestUI:
    @allure.step("Проверка открытия главной страницы")
    def test_open_homepage(self, driver):
        page = SearchPage(driver)
        page.open(settings.BASE_URL)
        title = page.get_page_title()
        assert "Кинопоиск" in title

    @allure.step("Поиск фильма")
    def test_search_movie(self, driver):
        page = SearchPage(driver)
        page.open(settings.BASE_URL)
        page.search("Интерстеллар")
        assert "Интерстеллар" in page.get_first_result()

    @allure.step("Открытие раздела Билеты в кино")
    def test_page_title(self, driver):
        page = SearchPage(driver)
        page.open(settings.BASE_URL_CINEMA)
        title = page.get_page_title()
        assert "Билеты в кино" in title

    @allure.step("Проверка поля поиска")
    def test_search_field_exists(self, driver):
        page = SearchPage(driver)
        page.open(settings.BASE_URL)
        assert driver.find_element(*SearchPage.SEARCH_INPUT)

    @allure.step("Открытие раздела Медиа")
    def test_open_media(self, driver):
        page = SearchPage(driver)
        page.open(settings.BASE_URL_MEDIA)
        title = page.get_page_title()
        assert "Медиа" in title
