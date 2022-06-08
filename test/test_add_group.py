# -*- coding: utf-8 -*-

import random
import string

import pytest

from model.group import Group


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    random_str = prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    return random_str


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string('name_', 10), header=random_string('header_', 5), footer=random_string('footer_', 5))
    for i in range(3)
]


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
