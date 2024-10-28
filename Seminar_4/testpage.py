from lxml.saxparser import element

from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

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
# функция для ввода текста
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.info(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Element while operation with {locator}")
            return False
        return True

# МЕТОДЫ ВВОДА ТЕКСТА
# поиск поля логин, очистка поля логин, ввод в поле теста
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_LOGIN_FIELD, word, description="login form")

# посик поля пароль, очистка поля пароль, ввод текста
    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

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

# поиск элемента имя, очистка, ввод текста
    def enter_your_name(self, your_name):
        input = self.find_element(TestSearchLocators.LOCATOR_YOUR_NAME)
        input.clear()
        input.send_keys(your_name)

# поиск элемента email, очистка, ввод текста
    def enter_your_email(self, your_email):
        input = self.find_element(TestSearchLocators.LOCATOR_YOUR_EMAIL)
        input.clear()
        input.send_keys(your_email)

# поиск элемента контента сообщения, очистка, ввод текста
    def enter_content_text(self, content_text):
        input = self.find_element(TestSearchLocators.LOCATOR_CONTENT_TEXT)
        input.clear()
        input.send_keys(content_text)

# МЕТОДЫ КЛИКА ПО КНОПКЕ
# поиск кнопки, клик по кнопке
    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

# поиск кнопки создания поста, нажатие кнопки
    def click_new_post_btn(self):
        self.find_element(TestSearchLocators.LOCATOR_NEW_BTN).click()

# поиск кнопки save, нажатие кнопки
    def click_save_btn(self):
        self.find_element(TestSearchLocators.LOCATOR_SAVE_BTN).click()

# клик по кнопке contact us для отправки сообщения
    def click_contact_us(self):
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US).click()

# МЕТОДЫ ДЛЯ ВЫВОДА ТЕКСТОВЫХ СООБЩЕНИЙ
# поиск элемента об ошибки, проверка вывода текста ошибки
    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

# поиск элемента имя пользователя, проверка вывода текста Hellow, ...
    def get_user_text(self):
        user_field = self.find_element(TestSearchLocators.LOCATOR_HELLO, time=3)
        text = user_field.text
        return text

# поиск элемента названия поста после сохранения с проверкой текста названия поста
    def get_res_text(self):
        res_field = self.find_element(TestSearchLocators.LOCATOR_POST_TITLE, time=3)
        text = res_field.text
        return text

# вывод окна алерт с текстом Exception with alert
    def get_alert_message(self):
         try:
             alert = self.driver.switch_to.alert
             return alert.text
         except:
             logging.exception("Exception with alert")
             return None




