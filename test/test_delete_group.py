from model.group import Group


def test_delete_first_group(app):
    print("\n\n*********** Test delete first group **********")

    # Обеспечение выполнения предусловий
    if app.group.count() == 0:
        app.group.create(Group(name="Precondition"))

    old_groups = app.group.get_group_list()
    app.group.delete_first()
    new_groups = app.group.get_group_list()
    assert len(new_groups) == len(old_groups) - 1
