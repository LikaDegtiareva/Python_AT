from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

class TestSearchLocators:
    LOCATOR_CONTENT_TEXT = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US = (By.XPATH, """//*[@id="contact"]/div[4]/button/span""")
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.XPATH, """//*[@id="login"]/div[3]/button/div""")
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
        logging.debug(f"Send {word} to element {element_name}")
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

# функция для вывода текста и текстовых сообщений
    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=2)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Element while get test from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text

# функция для клика по кнопке
    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return  False
        try:
            button.click()
        except:
            logging.exception(f"Exception with clik")
            return False
        logging.debug(f"Click button {element_name}")
        return True


# МЕТОДЫ ВВОДА ТЕКСТА
# поиск поля логин, очистка поля логин, ввод в поле теста
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_LOGIN_FIELD, word, description="login form")

# посик поля пароль, очистка поля пароль, ввод текста
    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_PASS_FIELD, word, description="password form")

# поиск элемента titlt, очистка поля, ввод текста
    def enter_title(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_TITLE, word, description="title")

# поиск элемента description, очистка поля, ввод текста
    def enter_description(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_DESCRIPTION, word, description="description")

# поиск элемента content, очистка поля, ввод текста
    def enter_content(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_CONTENT, word, description="content")

# поиск элемента имя, очистка, ввод текста
    def enter_your_name(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_YOUR_NAME, word, description="your name")

# поиск элемента email, очистка, ввод текста
    def enter_your_email(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_YOUR_EMAIL, word, description="email")

# поиск элемента контента сообщения, очистка, ввод текста
    def enter_content_text(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_CONTENT_TEXT, word, description="content_text")

# МЕТОДЫ КЛИКА ПО КНОПКЕ
# поиск кнопки, клик по кнопке
    def click_login_button(self):
        self.click_button(TestSearchLocators.LOCATOR_LOGIN_BTN, description="login_button")

# поиск кнопки создания поста, нажатие кнопки
    def click_new_post_btn(self):
        self.click_button(TestSearchLocators.LOCATOR_NEW_BTN, description="new_post_btn")

# поиск кнопки save, нажатие кнопки
    def click_save_btn(self):
        self.click_button(TestSearchLocators.LOCATOR_SAVE_BTN, description="save_btn")

# клик по кнопке contact us для отправки сообщения
    def click_contact_us(self):
        self.click_button(TestSearchLocators.LOCATOR_CONTACT_US, description="contact_us_btn")

# МЕТОДЫ ДЛЯ ВЫВОДА ТЕКСТОВЫХ СООБЩЕНИЙ
# поиск элемента об ошибки, проверка вывода текста ошибки
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.LOCATOR_ERROR_FIELD, description="error_text")

# поиск элемента имя пользователя, проверка вывода текста Hellow, ...
    def get_user_text(self):
        return self.get_text_from_element(TestSearchLocators.LOCATOR_HELLO, description="user_text")

# поиск элемента названия поста после сохранения с проверкой текста названия поста
    def get_res_text(self):
        return self.get_text_from_element(TestSearchLocators.LOCATOR_POST_TITLE, description="res_text")


# ВЫВОД ОКНА АЛЕРТ С СООБЩЕНИЕМ: Exception with alert
    def get_alert_message(self):
         try:
             alert = self.driver.switch_to.alert
             return alert.text
         except:
             logging.exception("Exception with alert")
             return None




