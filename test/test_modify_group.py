# -*- coding: utf-8 -*-

import logging.config
from random import randrange

from model.group import Group

logging.config.fileConfig('../log.conf')
log = logging.getLogger('simple')


def test_modify_group_name(app):
    log.debug("************ Test modify group name **********")

    # Обеспечение выполнения предусловий
    if app.group.count() == 0:
        app.group.create(Group(name="Precondition"))

    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(id=old_groups[index].id, name="New group name")
    app.group.modify_group_by_index(index, group)

    new_groups = app.group.get_group_list()
    assert len(new_groups) == len(old_groups)

    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_header(app):
    log.debug("*********** Test modify group header *********")
    old_groups = app.group.get_group_list()
    app.group.modify_first(Group(header="New group header"))
    new_groups = app.group.get_group_list()
    assert len(new_groups) == len(old_groups)


def test_modify_group_footer(app):
    log.debug("*********** Test modify group footer *********")
    old_groups = app.group.get_group_list()
    app.group.modify_first(Group(footer="New group footer"))
    new_groups = app.group.get_group_list()
    assert len(new_groups) == len(old_groups)


def test_modify_group_name_and_header(app):
    log.debug("********* Modify group name and header *******")
    old_groups = app.group.get_group_list()
    app.group.modify_first(Group(name="New group name", header="New group header"))
    new_groups = app.group.get_group_list()
    assert len(new_groups) == len(old_groups)


def test_modify_group_name_header_footer(app):
    log.debug("******** Modify group name/header/footer *****")
    old_groups = app.group.get_group_list()
    app.group.modify_first(Group(name="New name", header="New header", footer="New footer"))
    new_groups = app.group.get_group_list()
    assert len(new_groups) == len(old_groups)
