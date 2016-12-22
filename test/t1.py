def test_test(app):
    app.session.login(username="admin", password="secret")

    app.session.logout()