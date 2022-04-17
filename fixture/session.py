# -*- coding: utf-8 -*-

class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        print("Вспомогательный метод login()")
        print("  username: " + username)
        print("  password: " + password)
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        print("Вспомогательный метод logout()")
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
