import yaml
from selenium.webdriver.common.actions.interaction import Pause

class WebPage:
    def __init__(self, data):
        self.address = data['address']
        self.browser = data['browser']

class User:
    def __init__(self, data):
        self.login = data['login']
        self.password = data['password']

class Pause:
    def __init__(self, data):
        self.wait = data['wait']
        self.sleep = data['sleep']


class Post:
    def __init__(self, data):
        self.title = data['title']
        self.description = data['description']
        self.content = data['content']

class Config:
    def __init__(self, config_file="config.yaml"):
        with open(config_file) as f:
            self.data = yaml.safe_load(f)

    def web_page(self):
        return WebPage(self.data["web_page"])

    def user(self, user='user'):
        return User(self.data[user])

    def pause(self):
        return Pause(self.data["pause"])

    def post(self, index):
        return Post(self.data["post"][index])


