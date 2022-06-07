# -*- coding: utf-8 -*-

from model.group import Group


# Тестовые функции в качестве параметра будут принимать фикстуру,
# т.е. объект созданный функцией app()
def test_add_group(app):
    print("\n\n*************** Test add group ***************")
    old_groups = app.group.get_group_list()
    group = Group(name="Name 1", header="Header 1", footer="Footer 1")
    app.group.create(group)
    assert app.group.count() == len(old_groups) + 1

    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_empty_group(app):
    print("\n\n************ Test add empty group ************")
    old_groups = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)

    new_groups = app.group.get_group_list()
    assert len(new_groups) == len(old_groups) + 1

    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
