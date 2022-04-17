# -*- coding: utf-8 -*-

import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture  # чтобы pytest догадался, что это не просто функция, а функция создающая фикстуру
def app(request):
    print("\n\n*********** Инициализатор фикстуры ***********")
    fixture = Application()  # создать фикстуру
    request.addfinalizer(fixture.destroy)  # pytest сам вызовет в нужный момент для разрушения фикстуры
    return fixture  # вернуть фикстуру


# Тестовые функции в качестве параметра будут принимать фикстуру, т.е. объект созданный функцией app()
def test_add_group(app):
    print("\n\n*************** Test add group ***************")
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Name 1", header="Header 1", footer="Footer 1"))
    app.session.logout()


def test_add_empty_group(app):
    print("\n\n************ Test add empty group ************")
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
