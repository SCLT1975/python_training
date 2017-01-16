from model.group import Group


def test_adv_modify_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="251", header="578", footer="fhfkfh"))
    old_groups = app.group.get_group_list()
    app.group.modify(Group(name="New Group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups)  == len(new_groups)

def test_adv_modify_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="251", header="578", footer="fhfkfh"))
    old_groups = app.group.get_group_list()
    app.group.modify(Group(header="New_header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups)  == len(new_groups)
