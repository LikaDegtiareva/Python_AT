import requests

from Config import Config
from Validate import validate_status_200


class BaseApi:
    def __init__(self):
        self.connection = Config()
        self.x_auth_token = {"X-Auth-Token": self.login()}

    def login(self):
        url = self.connection.host + "/gateway/login"
        response = requests.post(
            url=url,
            data={"username":self.connection.username, "password": self.connection.password}
        )
        validate_status_200(response, "Ошибка запроса HTTP {}: {}".format(url, str(response.status_code)))
        return response.json()["token"]

    def get_not_my_posts(self, post_id):
        return self.get("/api/posts/" + post_id, {'owner': "notMe"})

    def get(self, page, query_params):
        url = self.connection.host + page
        response = requests.get(url, params=query_params, headers=self.x_auth_token)
        validate_status_200(response, "Ошибка запроса HTTP {}: {}".format(url, str(response.status_code)))
        return response.json()

    def new_post(self, post):
        url = self.connection.host + "/api/posts"
        response = requests.post(url, headers=self.x_auth_token, data=post)
        validate_status_200(response, "Ошибка запроса HTTP {}: {}".format(url, str(response.status_code)))
        return response.json()["id"]

    def get_post(self, post_id):
        url = self.connection.host + "/api/posts/" + str(post_id)
        response = requests.get(url, headers=self.x_auth_token)
        validate_status_200(response, "Ошибка запроса HTTP {}: {}".format(url, str(response.status_code)))
        return response.json()
