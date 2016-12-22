# -*- coding: utf-8 -*-

from model.group import Group



def test_test_add_group1(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="2341", header="wafasdfsadf", footer="fhfghfdghfdgh"))
    app.session.logout()


def test_test_empty_group1(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()



