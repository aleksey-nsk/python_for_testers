# -*- coding: utf-8 -*-

import pytest

# from data.add_group import testdata
from data.add_group import constant as testdata
from model.group import Group


# Тестовые функции в качестве параметра будут принимать фикстуру,
# т.е. объект созданный функцией app()
#
# С помощью @pytest.mark.parametrize()
# добавляем тестовые данные

@pytest.mark.parametrize('group', testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    print("\n\n*************** Test add group ***************")

    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert app.group.count() == len(old_groups) + 1

    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
