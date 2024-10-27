from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://test-stand.gb.ru"

# метод поиска элементов, зная метод и путь
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

# метод получения свойств элемента
    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        return element.value_of_css_property(property)

# метод открытия страницы сайта
    def go_to_site(self):
        return self.driver.get(self.base_url)

    def go_to_page(self, page):
        return self.driver.get(self.base_url + page)