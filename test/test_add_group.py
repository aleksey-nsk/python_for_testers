# -*- coding: utf-8 -*-

import logging.config

from model.group import Group

logging.config.fileConfig('../log.conf')
log = logging.getLogger('simple')


def test_add_group(app, db, json_groups):
    log.debug("*************** Test add group ***************")
    group = json_groups

    old_groups = db.get_group_list()
    app.group.create(group)
    assert app.group.count() == len(old_groups) + 1

    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
