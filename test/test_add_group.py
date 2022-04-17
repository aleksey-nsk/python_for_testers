# -*- coding: utf-8 -*-

from model.group import Group


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
