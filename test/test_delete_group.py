def test_delete_first_group(app):
    print("\n\n*********** Test delete first group **********")
    app.session.login(username="admin", password="secret")
    app.group.delete_first()
    app.session.logout()
