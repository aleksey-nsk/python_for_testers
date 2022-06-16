# -*- coding: utf-8 -*-

import logging.config

from selenium import webdriver

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.navigation import NavigationHelper
from fixture.session import SessionHelper

logging.config.fileConfig('../log.conf')
log = logging.getLogger('simple')


class Application:
    # В конструкторе инициализация. Здесь запускаем браузер:
    def __init__(self, browser, base_url):
        log.debug("Конструктор класса Application")

        if browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        else:
            raise ValueError('Unrecognized browser %s' % browser)

        # Неявное ожидание 5 секунд:
        self.wd.implicitly_wait(5)

        # Инициализируем помощников:
        self.session = SessionHelper(self)  # SessionHelper получает ссылку на объект класса Application
        self.group = GroupHelper(self)
        self.navigation = NavigationHelper(self, base_url)
        self.contact = ContactHelper(self)

    def stop_browser(self):
        log.debug("Вспомогательный метод stop_browser(). Останавливаем браузер")
        self.wd.quit()

    def is_valid(self):
        log.debug("Вспомогательный метод is_valid()")
        try:
            self.wd.current_url
            log.debug("  фикстура валидна")
            return True
        except:
            log.debug("  фикстура не валидна")
            return False
