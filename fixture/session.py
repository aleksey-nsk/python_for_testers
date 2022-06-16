# -*- coding: utf-8 -*-

import logging.config
import time

logging.config.fileConfig('../log.conf')
log = logging.getLogger('simple')


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        log.debug("  вспомогательный метод login(). Username: " + username + ", password: " + password)
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath('//input[@value="Login"]').click()

    def logout(self):
        log.debug("  вспомогательный метод logout()")
        wd = self.app.wd
        time.sleep(1)  # пауза 1 секунда
        wd.find_element_by_link_text("Logout").click()
        time.sleep(1)  # пауза 1 секунда

    def is_logged_in(self):
        wd = self.app.wd
        boolean = len(wd.find_elements_by_link_text("Logout")) > 0
        log.debug("  вспомогательный метод is_logged_in(). Залогинен: " + str(boolean))
        return boolean

    def is_logged_in_as(self, username):
        log.debug('  вспомогательный метод is_logged_in_as(), username: ' + username)
        return self.get_logged_user() == username

    def get_logged_user(self):
        log.debug('  вспомогательный метод get_logged_user()')
        wd = self.app.wd
        actual_user = wd.find_element_by_xpath("//div[@id='container']/div[@id='top']/form/b").text[1:-1]
        log.debug('  actual_user: ' + actual_user)
        return actual_user

    def ensure_login(self, username, password):
        log.debug("Вспомогательный метод ensure_login()")

        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()

        self.login(username, password)

    def ensure_logout(self):
        log.debug("Вспомогательный метод ensure_logout()")
        time.sleep(1)  # пауза 1 секунда
        if self.is_logged_in():
            self.logout()
