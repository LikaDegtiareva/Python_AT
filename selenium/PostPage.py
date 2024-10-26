import time

class PostPage:
    def __init__(self, site, config):
        self.site = site
        self.config = config

    def create(self,
               create_post_selector="""//*[@id="create-btn"]""",
               title_selector="""//*[@id="create-item"]/div/div/div[1]/div/label/input""",
               description_selector="""//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""",
               content_selector="""//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""",
               save_btn_selector="""//*[@id="create-item"]/div/div/div[7]/div/button/span"""
               ):
        new_post_btn = self.site.find_element("xpath", create_post_selector)
        new_post_btn.click()
        title_input = self.site.find_element("xpath", title_selector)
        post = self.config.post(0)
        title_input.send_keys(post.title)
        description_input = self.site.find_element("xpath", description_selector)
        description_input.send_keys(post.description)
        content_input = self.site.find_element("xpath", content_selector)
        content_input.send_keys(post.content)
        pause = self.config.pause()
        time.sleep(pause.sleep)
        save_btn = self.site.find_element("xpath", save_btn_selector)
        save_btn.click()
        time.sleep(pause.sleep)
        return post
