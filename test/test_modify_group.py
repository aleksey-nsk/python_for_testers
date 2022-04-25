# -*- coding: utf-8 -*-

from model.group import Group


def test_modify_group_name(app):
    print("\n\n************ Test modify group name **********")
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(name="New group name"))
    app.session.logout()


def test_modify_group_header(app):
    print("\n\n*********** Test modify group header *********")
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(header="New group header"))
    app.session.logout()


def test_modify_group_footer(app):
    print("\n\n*********** Test modify group footer *********")
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(footer="New group footer"))
    app.session.logout()


def test_modify_group_name_and_header(app):
    print("\n\n********* Modify group name and header *******")
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(name="New group name", header="New group header"))
    app.session.logout()


def test_modify_group_name_header_footer(app):
    print("\n\n******** Modify group name/header/footer *****")
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(name="New name", header="New header", footer="New footer"))
    app.session.logout()
