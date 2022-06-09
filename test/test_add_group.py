# -*- coding: utf-8 -*-

from model.group import Group


# Тестовые функции в качестве параметра будут принимать фикстуру,
# т.е. объект созданный функцией app()
def test_add_group(app, json_groups):
    print("\n\n*************** Test add group ***************")
    group = json_groups

    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert app.group.count() == len(old_groups) + 1

    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
