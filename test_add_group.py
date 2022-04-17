# -*- coding: utf-8 -*-

import unittest

from application import Application
from group import Group


class GroupCreationTests(unittest.TestCase):
    # Данный метод будет инициализировать фикстуру:
    def setUp(self):
        print("\n\n******************* setUp ********************")
        self.app = Application()

    # Метод завершения:
    def tearDown(self):
        print("\n\n****************** tearDown ******************")
        self.app.destroy()

    def test_add_group(self):
        print("\n\n*************** Test add group ***************")
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="Name 1", header="Header 1", footer="Footer 1"))
        self.app.logout()

    def test_add_empty_group(self):
        print("\n\n************ Test add empty group ************")
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="", header="", footer=""))
        self.app.logout()


# Подсказка для Python как именно этот скрипт должен запускаться, в том случае если мы
# не указываем явно, что он должен быть запущен при помощи утилиты py.test (py.test test_add_group.py),
# а просто пишем (python test_add_group.py)
#
# Python посмотрит на эти строчки, увидит что нужно запустить unittest (unittest.main()),
# и запустит его. Далее unittest найдёт тестовый класс, тестовый метод, и выполнит их:
if __name__ == "__main__":
    unittest.main()
