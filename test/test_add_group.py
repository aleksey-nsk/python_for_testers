# -*- coding: utf-8 -*-

from model.group import Group


# Тестовые функции в качестве параметра будут принимать фикстуру,
# т.е. объект созданный функцией app()
def test_add_group(app):
    print("\n\n*************** Test add group ***************")
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="Name 1", header="Header 1", footer="Footer 1"))
    new_groups = app.group.get_group_list()
    assert len(new_groups) == len(old_groups) + 1


def test_add_empty_group(app):
    print("\n\n************ Test add empty group ************")
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(new_groups) == len(old_groups) + 1
