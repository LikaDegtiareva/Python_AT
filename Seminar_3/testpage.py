from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

logger = logging.getLogger(__name__)

class Parameters:
    your_name = "name"
    your_email = "my_name@mail.ru"
    content_text = "testcontent"
    any_text = "test"
    unknown_password = "test"
    unknown_user = "test"
    browser = "chrome"
    sleep_time = 1
    wait = 3
    username = "Kukumber@"
    password = "116c74cc50"

class TestSearchLocators:
    LOCATOR_CONTENT_TEXT = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US = (By.XPATH, """//*[@id="contact"]/div[4]/button/span""")
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, """button""")
    LOCATOR_ERROR_FIELD =  (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_HELLO = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_NEW_BTN = (By.XPATH, """//*[@id="create-btn"]""")
    LOCATOR_TITLE = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_DESCRIPTION = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_CONTENT = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_SAVE_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button/span""")
    LOCATOR_POST_TITLE = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_YOUR_NAME = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_YOUR_EMAIL = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")


class OperationsHelper(BasePage):
# поиск поля логин, очистка поля логин, ввод в поле теста
    def enter_login(self, word):
        logger.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

# посик поля пароль, очистка поля пароль, ввод текста
    def enter_pass(self, word):
        logger.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

# поиск кнопки, клик по кнопке
    def click_login_button(self):
        logger.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

# поиск элемента об ошибки, проверка вывода текста ошибки
    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logger.info(f"We find text '{text}' in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

# поиск элемента имя пользователя, проверка вывода текста Hellow, ...
    def get_user_text(self):
        user_field = self.find_element(TestSearchLocators.LOCATOR_HELLO, time=3)
        text = user_field.text
        return text

# поиск кнопки создания поста, нажатие кнопки
    def click_new_post_btn(self):
        self.find_element(TestSearchLocators.LOCATOR_NEW_BTN).click()

# поиск элемента titlt, очистка поля, ввод текста
    def enter_title(self, word):
        login_field = self.find_element(TestSearchLocators.LOCATOR_TITLE)
        login_field.clear()
        login_field.send_keys(word)

# поиск элемента description, очистка поля, ввод текста
    def enter_description(self, word):
        login_field = self.find_element(TestSearchLocators.LOCATOR_DESCRIPTION)
        login_field.clear()
        login_field.send_keys(word)

# поиск элемента content, очистка поля, ввод текста
    def enter_content(self, word):
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT)
        login_field.clear()
        login_field.send_keys(word)

# поиск кнопки save, нажатие кнопки
    def click_save_btn(self):
        self.find_element(TestSearchLocators.LOCATOR_SAVE_BTN).click()

# поиск элемента названия поста после сохранения
    def get_res_text(self):
        res_field = self.find_element(TestSearchLocators.LOCATOR_POST_TITLE, time=3)
        text = res_field.text
        return text

    def get_alert_message(self):
        return self.driver.switch_to.alert.text

    def enter_your_name(self, your_name):
        input = self.find_element(TestSearchLocators.LOCATOR_YOUR_NAME)
        input.clear()
        input.send_keys(your_name)

    def enter_your_email(self, your_email):
        input = self.find_element(TestSearchLocators.LOCATOR_YOUR_EMAIL)
        input.clear()
        input.send_keys(your_email)

    def enter_content_text(self, content_text):
        input = self.find_element(TestSearchLocators.LOCATOR_CONTENT_TEXT)
        input.clear()
        input.send_keys(content_text)

    def click_contact_us(self):
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US).click()










