# -*- coding: utf-8 -*-

import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_group1(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="2341", header="wafasdfsadf", footer="fhfghfdghfdgh"))
    app.session.logout()


def test_test_empty_group1(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()



