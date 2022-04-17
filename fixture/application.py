# -*- coding: utf-8 -*-

from selenium import webdriver

from fixture.group import GroupHelper
from fixture.navigation import NavigationHelper
from fixture.session import SessionHelper


class Application:
    # В конструкторе инициализация. Здесь запускаем браузер:
    def __init__(self):
        print("Конструктор класса Application")
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(10)
        # Инициализируем помощников:
        self.session = SessionHelper(self)  # SessionHelper получает ссылку на объект класса Application
        self.group = GroupHelper(self)
        self.navigation = NavigationHelper(self)

    # Вспомогательный метод для разрушения фикстуры. Здесь останавливаем браузер:
    def destroy(self):
        print("Вспомогательный метод destroy(). Разрушаем фикстуру")
        self.wd.quit()
