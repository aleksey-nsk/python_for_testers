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

    def open_home_page(self):
        print("  вспомогательная функция open_home_page()")
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def login(self, username, password):
        print("  вспомогательная функция login()")
        print("    username: " + username)
        print("    password: " + password)
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_groups_page(self):
        print("  вспомогательная функция open_groups_page()")
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def create_group(self, group):
        print("  вспомогательная функция create_group()")
        print("    group: " + str(group))
        wd = self.wd
        self.open_groups_page()
        # Init group creation:
        wd.find_element_by_name("new").click()
        # Fill group form:
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Submit group creation:
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        print("  вспомогательная функция return_to_groups_page()")
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def logout(self):
        print("  вспомогательная функция logout()")
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def test_add_group(self):
        print("Test add group")
        self.login(username="admin", password="secret")
        self.create_group(Group(name="Name 1", header="Header 1", footer="Footer 1"))
        self.logout()

    def test_add_empty_group(self):
        print("Test add empty group")
        self.login(username="admin", password="secret")
        self.create_group(Group(name="", header="", footer=""))
        self.logout()


# Подсказка для Python как именно этот скрипт должен запускаться, в том случае если мы
# не указываем явно, что он должен быть запущен при помощи утилиты py.test (py.test test_add_group.py),
# а просто пишем (python test_add_group.py)
#
# Python посмотрит на эти строчки, увидит что нужно запустить unittest (unittest.main()),
# и запустит его. Далее unittest найдёт тестовый класс, тестовый метод, и выполнит их:
if __name__ == "__main__":
    unittest.main()
