# -*- coding: utf-8 -*-

import unittest

from selenium import webdriver

from group import Group


# Пока будем использовать unittest - входит в стандартную библиотеку Python
# В unittest требуется чтобы тестовый класс являлся наследником специального класса - unittest.TestCase
class GroupCreationTests(unittest.TestCase):
    def setUp(self):
        print("\n\n********** setUp **********")
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def tearDown(self):
        print("********** tearDown **********\n")
        self.wd.quit()

    def open_home_page(self, wd):
        print("  вспомогательная функция open_home_page()")
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        print("  вспомогательная функция login()")
        print("    username: " + username)
        print("    password: " + password)
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_groups_page(self, wd):
        print("  вспомогательная функция open_groups_page()")
        wd.find_element_by_link_text("groups").click()

    def create_group(self, wd, group):
        print("  вспомогательная функция create_group()")
        print("    group: " + str(group))
        # Init group creation:
        wd.find_element_by_name("new").click()
        # Fill group form:
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Submit group creation:
        wd.find_element_by_name("submit").click()

    def return_to_groups_page(self, wd):
        print("  вспомогательная функция return_to_groups_page()")
        wd.find_element_by_link_text("group page").click()

    def logout(self, wd):
        print("  вспомогательная функция logout()")
        wd.find_element_by_link_text("Logout").click()

    def test_add_group(self):
        print("Test add group")
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_groups_page(wd)
        self.create_group(wd, Group(name="Name 1", header="Header 1", footer="Footer 1"))
        self.return_to_groups_page(wd)
        self.logout(wd)

    def test_add_empty_group(self):
        print("Test add empty group")
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_groups_page(wd)
        self.create_group(wd, Group(name="", header="", footer=""))
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
