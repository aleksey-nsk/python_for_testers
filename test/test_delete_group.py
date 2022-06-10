import random

from model.group import Group


def test_delete_some_group(app, db):
    print("\n\n*********** Test delete some group **********")

    # Обеспечение выполнения предусловий
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Precondition"))

    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    assert app.group.count() == len(old_groups) - 1

    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert new_groups == old_groups
