import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://test-stand.gb.ru"

# метод поиска элементов, зная метод и путь
    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")
        except:
            logging.exception("Find element exception")
            element = None
        return element

# метод получения свойств элемента
    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(property)
        else:
            logging.error(f"Property {property} not found in element with locator {locator}")
            return None

# метод открытия страницы сайта
    def go_to_site(self):
        try:
            start_browsing = self.driver.get(self.base_url)
        except:
            logging.exception("Exception while open site")
            start_browsing = None
        return start_browsing

# метод открытия страницы сайта
    def go_to_page(self, page):
        try:
            start_page = self.driver.get(self.base_url + page)
        except:
            logging.exception("Exception while open page")
            start_page = None
        return start_page

