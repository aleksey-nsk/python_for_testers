# -*- coding: utf-8 -*-

class NavigationHelper:
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        print("Вспомогательный метод open_home_page()")
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")
