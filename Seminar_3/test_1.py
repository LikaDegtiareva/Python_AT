import time

from testpage import OperationsHelper, Parameters
import logging

logger = logging.getLogger(__name__)
parameters = Parameters()

# ввести неверные логин и пароль, кликнуть по кнопке и проверить вывод ошибки 401
def test_step1(browser):
     logger.info("Test 1 Starting")
     testpage = OperationsHelper(browser)
     testpage.go_to_site()
     testpage.enter_login(parameters.unknown_user)
     testpage.enter_pass(parameters.unknown_password)
     testpage.click_login_button()
     assert testpage.get_error_text() == "401"

# ввести верные логин и пароль, кликнуть по кнопке и проверить вывод текста Hellow
def test_step2(browser):
     testpage = OperationsHelper(browser)
     testpage.enter_login(parameters.username)
     testpage.enter_pass(parameters.password)
     testpage.click_login_button()
     assert testpage.get_user_text() == f"Hello, " + parameters.username

# создать новый пост и проверить, наличие названия поста после его создания
def test_step3(browser):
     testpage = OperationsHelper(browser)
     testpage.click_new_post_btn()
     testpage.enter_title(parameters.any_text)
     testpage.enter_description(parameters.any_text)
     testpage.enter_content(parameters.any_text)
     testpage.click_save_btn()
     time.sleep(2)
     assert testpage.get_res_text() == parameters.any_text

def test_step4(browser):
     testpage = OperationsHelper(browser)
     testpage.go_to_page("/contact")
     time.sleep(2)
     testpage.enter_your_name(parameters.your_name)
     testpage.enter_your_email(parameters.your_email)
     testpage.enter_content_text(parameters.content_text)
     testpage.click_contact_us()
     time.sleep(2)
     message = testpage.get_alert_message()
     assert "Form successfully submitted" == message


# css_selector = "span.mdc-text-field__ripple"
# print(site.get_element_property("css", css_selector, "height"))

# xpath = '//*[@id="login"]/div[3]/button/span'
# print(site.get_element_property("xpath", xpath, "color"))

