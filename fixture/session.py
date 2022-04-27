# -*- coding: utf-8 -*-

import time


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        print("  вспомогательный метод login(). Username: " + username + ", password: " + password)
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        print("  вспомогательный метод logout()")
        wd = self.app.wd
        time.sleep(1)  # пауза 1 секунда
        wd.find_element_by_link_text("Logout").click()
        time.sleep(1)  # пауза 1 секунда

    def is_logged_in(self):
        wd = self.app.wd
        boolean = len(wd.find_elements_by_link_text("Logout")) > 0
        print("  вспомогательный метод is_logged_in(). Залогинен:", boolean)
        return boolean

    def is_logged_in_as(self, username):
        print("  вспомогательный метод is_logged_in_as(), username: " + username)
        wd = self.app.wd
        actual_text = wd.find_element_by_xpath("//div[@id='container']/div[@id='top']/form/b").text
        expected_text = "(" + username + ")"
        print("  actual_text: " + actual_text + ", expected_text: " + expected_text)
        return actual_text == expected_text

    def ensure_login(self, username, password):
        print("Вспомогательный метод ensure_login()")

        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()

        self.login(username, password)

    def ensure_logout(self):
        print("Вспомогательный метод ensure_logout()")
        time.sleep(1)  # пауза 1 секунда
        if self.is_logged_in():
            self.logout()
