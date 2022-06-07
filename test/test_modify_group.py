# -*- coding: utf-8 -*-

from model.group import Group


def test_modify_group_name(app):
    print("\n\n************ Test modify group name **********")
    old_groups = app.group.get_group_list()
    group = Group(id=old_groups[0].id, name="New group name")
    app.group.modify_first(group)

    new_groups = app.group.get_group_list()
    assert len(new_groups) == len(old_groups)

    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_header(app):
    print("\n\n*********** Test modify group header *********")
    old_groups = app.group.get_group_list()
    app.group.modify_first(Group(header="New group header"))
    new_groups = app.group.get_group_list()
    assert len(new_groups) == len(old_groups)


def test_modify_group_footer(app):
    print("\n\n*********** Test modify group footer *********")
    old_groups = app.group.get_group_list()
    app.group.modify_first(Group(footer="New group footer"))
    new_groups = app.group.get_group_list()
    assert len(new_groups) == len(old_groups)


def test_modify_group_name_and_header(app):
    print("\n\n********* Modify group name and header *******")
    old_groups = app.group.get_group_list()
    app.group.modify_first(Group(name="New group name", header="New group header"))
    new_groups = app.group.get_group_list()
    assert len(new_groups) == len(old_groups)


def test_modify_group_name_header_footer(app):
    print("\n\n******** Modify group name/header/footer *****")
    old_groups = app.group.get_group_list()
    app.group.modify_first(Group(name="New name", header="New header", footer="New footer"))
    new_groups = app.group.get_group_list()
    assert len(new_groups) == len(old_groups)
