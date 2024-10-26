from Authorization import Authorization
from PostPage import PostPage
from config import Config
from module import Site

config = Config("config.yaml")

# ввести неверные логин и пароль, кликнуть по кнопке и проверить вывод ошибки 401
def test_step1(error_login_selector, err_label):
    site = Site(config)
    auth = Authorization(site, config)
    auth.login(user_name='unknown_user')
    element = site.find_element("xpath", error_login_selector)
    text = element.text
    site.quit()
    assert text == err_label

# ввести верные логин и пароль, кликнуть по кнопке и проверить вывод текста Hellow
def test_step2(user_label_selector, user_greeting):
    site = Site(config)
    auth = Authorization(site, config)
    auth.login()
    user_element = site.find_element("xpath", user_label_selector)
    text = user_element.text
    site.quit()
    assert text == user_greeting

# создать новый пост и проверить, наличие названия поста после его создания
def test_step_3(post_title_selector):
    site = Site(config)
    auth = Authorization(site, config)
    auth.login()
    post_page = PostPage(site, config)
    post = post_page.create()
    text = site.find_element("xpath", post_title_selector).text
    site.quit()
    assert text == post.title
