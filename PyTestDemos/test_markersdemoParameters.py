import pytest
import sys


@pytest.mark.parametrize("username,password",
                         [
                             ("Selenium", "WebDriver",),
                             ("Python", "Pytest",),
                             ("Shokirbek", "Mya",)
                         ])
def test_login(username, password):
    print(username)
    print(password)
