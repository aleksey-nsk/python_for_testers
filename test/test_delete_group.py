from model.group import Group


def test_delete_first_group(app):
    print("\n\n*********** Test delete first group **********")

    # Обеспечение выполнения предусловий
    if app.group.count() == 0:
        app.group.create(Group(name="Precondition"))

    app.group.delete_first()
