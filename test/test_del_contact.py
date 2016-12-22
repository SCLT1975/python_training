# -*- coding: utf-8 -*-

def test_test_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_1st()
    app.session.logout()