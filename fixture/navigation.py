# -*- coding: utf-8 -*-

class NavigationHelper:
    def __init__(self, app, base_url):
        self.app = app
        self.base_url = base_url

    def open_home_page(self):
        print("Вспомогательный метод open_home_page()")
        wd = self.app.wd
        wd.get(self.base_url)
