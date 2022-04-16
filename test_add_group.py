# -*- coding: utf-8 -*-

import unittest

from selenium import webdriver


# Пока будем использовать unittest - входит в стандартную библиотеку Python
# В unittest требуется чтобы тестовый класс являлся наследником специального класса - unittest.TestCase
class GroupCreationTests(unittest.TestCase):
    def setUp(self):
        print("\n***** setUp *****")
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def tearDown(self):
        print("***** tearDown *****")
        self.wd.quit()

    def open_home_page(self, wd):
        print("  вспомогательная функция open_home_page()")
        wd.get("http://localhost/addressbook/")

    def login(self, wd):
        print("  вспомогательная функция login()")
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_groups_page(self, wd):
        print("  вспомогательная функция open_groups_page()")
        wd.find_element_by_link_text("groups").click()

    def create_group(self, wd):
        print("  вспомогательная функция create_group()")
        # Init group creation:
        wd.find_element_by_name("new").click()
        # Fill group form:
        wd.find_element_by_name("group_name").send_keys("Name 1")
        wd.find_element_by_name("group_header").send_keys("Header 1")
        wd.find_element_by_name("group_footer").send_keys("Footer 1")
        # Submit group creation:
        wd.find_element_by_name("submit").click()

    def return_to_groups_page(self, wd):
        print("  вспомогательная функция return_to_groups_page()")
        wd.find_element_by_link_text("group page").click()

    def logout(self, wd):
        print("  вспомогательная функция logout()")
        wd.find_element_by_link_text("Logout").click()

    def test_group_creation(self):
        print("Test group creation")
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.open_groups_page(wd)
        self.create_group(wd)
        self.return_to_groups_page(wd)
        self.logout(wd)


# Подсказка для Python как именно этот скрипт должен запускаться, в том случае если мы
# не указываем явно, что он должен быть запущен при помощи утилиты py.test (py.test test_add_group.py),
# а просто пишем (python test_add_group.py)
#
# Python посмотрит на эти строчки, увидит что нужно запустить unittest (unittest.main()),
# и запустит его. Далее unittest найдёт тестовый класс, тестовый метод, и выполнит их:
if __name__ == "__main__":
    unittest.main()
