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
    app.login(username="admin", password="secret")
    app.create_new_group(Group(name="2341", header="wafasdfsadf", footer="fhfghfdghfdgh"))
    app.logout()


def test_test_empty_group1(app):
    app.login(username="admin", password="secret")
    app.create_new_group(Group(name="", header="", footer=""))
    app.logout()



