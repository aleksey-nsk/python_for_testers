# -*- coding: utf-8 -*-

from model.group import Group


def test_modify_group_name(app):
    print("\n\n************ Test modify group name **********")
    app.group.modify_first(Group(name="New group name"))


def test_modify_group_header(app):
    print("\n\n*********** Test modify group header *********")
    app.group.modify_first(Group(header="New group header"))


def test_modify_group_footer(app):
    print("\n\n*********** Test modify group footer *********")
    app.group.modify_first(Group(footer="New group footer"))


def test_modify_group_name_and_header(app):
    print("\n\n********* Modify group name and header *******")
    app.group.modify_first(Group(name="New group name", header="New group header"))


def test_modify_group_name_header_footer(app):
    print("\n\n******** Modify group name/header/footer *****")
    app.group.modify_first(Group(name="New name", header="New header", footer="New footer"))
