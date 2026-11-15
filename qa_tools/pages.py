from abc import ABC, abstractmethod
import json
from day71 import TestResult


class BasePage:
    def __init__(self,url):
        self.url = url

    def open(self):
        return f"open {self.url}"

class LoginPage(BasePage):
    def __init__(self, url, username_field):
        super().__init__(url)
        self.username_field = username_field

    def login(self, user, password):
        return f"{self.open()} and login as  {user}"

    def open(self):
        print(super().open())
        return f"hahaha!!!"

class AccountPage(BasePage):
    def __init__(self, url, title):
        super().__init__(url)
        self.title = title

    def get_title(self):
        return f"I returned a title; {self.title}"