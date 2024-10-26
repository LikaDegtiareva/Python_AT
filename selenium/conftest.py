import pytest

@pytest.fixture
def error_login_selector():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""

@pytest.fixture
def err_label():
    return "401"


@pytest.fixture
def user_label_selector():
    return """//*[@id="app"]/main/nav/ul/li[3]/a"""


@pytest.fixture
def user_greeting():
    return "Hello, {}".format("Kukumber@")

@pytest.fixture
def post_title_selector():
    return """//*[@id="app"]/main/div/div[1]/h1"""




