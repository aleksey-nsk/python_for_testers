# -*- coding: utf-8 -*-

from selenium import webdriver

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.navigation import NavigationHelper
from fixture.session import SessionHelper


class Application:
    # В конструкторе инициализация. Здесь запускаем браузер:
    def __init__(self, browser, base_url):
        print("Конструктор класса Application")

        if browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        else:
            raise ValueError('Unrecognized browser %s' % browser)

        self.wd.implicitly_wait(5)  # неявное ожидание 5 секунд
        # Инициализируем помощников:
        self.session = SessionHelper(self)  # SessionHelper получает ссылку на объект класса Application
        self.group = GroupHelper(self)
        self.navigation = NavigationHelper(self, base_url)
        self.contact = ContactHelper(self)

    def stop_browser(self):
        print("Вспомогательный метод stop_browser(). Останавливаем браузер")
        self.wd.quit()

    def is_valid(self):
        print("Вспомогательный метод is_valid()")
        try:
            self.wd.current_url
            print("  фикстура валидна")
            return True
        except:
            print("  фикстура не валидна")
            return False
