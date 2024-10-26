import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class Site:
# функция запуска веб-страницы
    def __init__(self, config):
        page = config.web_page()
        if page.browser == "firefox":
            service = Service(executable_path=GeckoDriverManager().install())
            options = webdriver.FirefoxOptions()
            self.driver = webdriver.Firefox(service=service, options=options)
        elif page.browser == "chrome":
            service = Service(executable_path=ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service=service, options=options)
        pause = config.pause()
        self.driver.implicitly_wait(pause.wait)
        self.driver.maximize_window()
        self.driver.get(page.address)
        time.sleep(pause.sleep)

# функция поиска элементов, зная метод и путь
    def find_element(self, mode, path):
        if mode == "css":
            element = self.driver.find_element(By.CSS_SELECTOR, path)
        elif mode == "xpath":
            element = self.driver.find_element(By.XPATH, path)
        else:
            element = None
        return element

# функция получения свойств элемента
    def get_element_property(self, mode, path, property):
        element = self.find_element(mode, path)
        return element.value_of_css_property(property)

# функция закрытия соединения
    def quit(self):
        self.driver.quit()