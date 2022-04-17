# -*- coding: utf-8 -*-

import pytest

from application import Application
from group import Group


@pytest.fixture  # чтобы pytest догадался, что это не просто функция, а функция создающая фикстуру
def app(request):
    print("\n\n*********** Инициализатор фикстуры ***********")
    fixture = Application()  # создать фикстуру
    request.addfinalizer(fixture.destroy)  # pytest сам вызовет в нужный момент для разрушения фикстуры
    return fixture  # вернуть фикстуру


# Тестовые функции в качестве параметра будут принимать фикстуру, т.е. объект созданный функцией app()
def test_add_group(app):
    print("\n\n*************** Test add group ***************")
    app.login(username="admin", password="secret")
    app.create_group(Group(name="Name 1", header="Header 1", footer="Footer 1"))
    app.logout()


def test_add_empty_group(app):
    print("\n\n************ Test add empty group ************")
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
