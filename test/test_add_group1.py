# -*- coding: utf-8 -*-

from model.group import Group



def test_test_add_group1(app):
    app.group.create(Group(name="2341", header="wafasdfsadf", footer="fhfghfdghfdgh"))


def test_test_empty_group1(app):
    app.group.create(Group(name="", header="", footer=""))


