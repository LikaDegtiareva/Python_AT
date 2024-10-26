class Authorization:
    def __init__(self, site, config):
        self.config = config
        self.site = site

    def login(self,
              user_name='user',
              login_selector="""//*[@id="login"]/div[1]/label/input""",
              password_selector="""//*[@id="login"]/div[2]/label/input""",
              button_selector="""button"""
              ):
        user = self.config.user(user_name)
        input_login = self.site.find_element("xpath", login_selector)
        input_login.send_keys(user.login)
        input_passw = self.site.find_element("xpath", password_selector)
        input_passw.send_keys(user.password)
        button = self.site.find_element("css", button_selector)
        button.click()


