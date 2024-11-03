import logging
import time

from BaseApi import BaseApi
from testpage import OperationsHelper


# ввести неверные логин и пароль, кликнуть по кнопке и проверить вывод ошибки 401
def test_step1(browser, config):
     logging.info("Test 1 Starting")
     testpage = OperationsHelper(browser)
     testpage.go_to_site()
     testpage.enter_login(config.unknown)
     testpage.enter_pass(config.unknown)
     testpage.click_login_button()
     assert testpage.get_error_text() == "401"

# ввести верные логин и пароль, кликнуть по кнопке и проверить вывод текста Hellow
def test_step2(browser, config):
     testpage = OperationsHelper(browser)
     testpage.go_to_site()
     testpage.enter_login(config.username)
     testpage.enter_pass(config.password)
     testpage.click_login_button()
     assert testpage.get_user_text() == (f"Hello, " + config.username)

# создать новый пост и проверить, наличие названия поста после его создания
def test_step3(browser, config):
     testpage = OperationsHelper(browser)
     testpage.click_new_post_btn()
     testpage.enter_title(config.sometext)
     testpage.enter_description(config.sometext)
     testpage.enter_content(config.sometext)
     testpage.click_save_btn()
     time.sleep(2)
     assert testpage.get_res_text() == config.sometext

def test_step4(browser, config):
     testpage = OperationsHelper(browser)
     testpage.go_to_page("/contact")
     time.sleep(2)
     testpage.enter_your_name(config.sometext)
     testpage.enter_your_email(config.email)
     testpage.enter_content_text(config.sometext)
     testpage.click_contact_us()
     time.sleep(2)
     message = testpage.get_alert_message()
     assert "Form successfully submitted" == message

def test_step5(some_post):
     api = BaseApi()
     user_post = api.get_not_my_posts(some_post['id'])
     #post_titles = [user_post["title"] for user_post in user_posts["data"]]
     assert some_post['title'] == user_post['title']


def test_step6(test_post):
     api = BaseApi()
     post_id = api.new_post(test_post)
     post = api.get_post(post_id)
     assert test_post['description'] == post['description']


