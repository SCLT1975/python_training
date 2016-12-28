from model.group import Group


def test_adv_modify_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="251", header="578", footer="fhfkfh"))
    app.group.modify(Group(name="New Group"))

def test_adv_modify_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="251", header="578", footer="fhfkfh"))
    app.group.modify(Group(header="New_header"))
