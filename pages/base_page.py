from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_kinopoisk_loaded(self):
        """Ждет полной загрузки Кинопоиска по логотипу"""
        # Ждем логотип для дополнительной уверенности
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "kinopoisk-header-logo__img"))
        )

    def open(self, url):
        """Открывает страницу и ждет ее загрузки"""
        self.driver.get(url)
        self.wait_for_kinopoisk_loaded()

    def get_page_title(self):
        """Возвращает текущий заголовок страницы"""
        return self.driver.title

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        elem = self.wait.until(EC.visibility_of_element_located(locator))
        elem.clear()
        elem.send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text
