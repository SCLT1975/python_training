# -*- coding: utf-8 -*-


def test_delete_1st_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_1st_group()
    app.session.logout()