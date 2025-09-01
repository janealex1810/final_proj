from selenium.webdriver.common.by import By
from .base_page import BasePage

class SearchPage(BasePage):
    SEARCH_INPUT = (By.NAME, "kp_query")
    RESULT_TITLE = (By.CLASS_NAME, "most_wanted")

    def search(self, query: str):
        self.enter_text(self.SEARCH_INPUT, query + "\n")

    def get_first_result(self):
        return self.get_text(self.RESULT_TITLE)
