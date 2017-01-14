# -*- coding: utf-8 -*-

from model.group import Group



def test_test_add_group1(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="2341", header="wafasdfsadf", footer="fhfghfdghfdgh"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

def test_test_empty_group1(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


