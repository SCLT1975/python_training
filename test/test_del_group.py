# -*- coding: utf-8 -*-
from model.group import Group

def test_delete_1st_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="Test"))
    app.group.delete_1st_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
