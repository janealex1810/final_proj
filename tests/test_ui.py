import pytest
import allure
from config import settings
from pages.search_page import SearchPage

@pytest.mark.ui
@allure.feature("UI Tests")
class TestUI:
    @allure.step("Проверка открытия главной страницы")
    def test_open_homepage(self, driver):
        driver.get(settings.BASE_URL)
        assert "Кинопоиск" in driver.title

    @allure.step("Поиск фильма")
    def test_search_movie(self, driver):
        page = SearchPage(driver)
        page.open(settings.BASE_URL)
        page.search("Интерстеллар")
        assert "Интерстеллар" in page.get_first_result()

    @allure.step("Проверка заголовка сайта")
    def test_page_title(self, driver):
        driver.get(settings.BASE_URL)
        assert "Кино" in driver.title

    @allure.step("Проверка поля поиска")
    def test_search_field_exists(self, driver):
        page = SearchPage(driver)
        page.open(settings.BASE_URL)
        assert driver.find_element(*SearchPage.SEARCH_INPUT)

    @allure.step("Открытие раздела Афиша")
    def test_open_afisha(self, driver):
        driver.get(settings.BASE_URL + "/afisha")
        assert "Афиша" in driver.title
