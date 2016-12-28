from model.group import Group


def test_adv_modify_name(app):
    app.group.modify(Group(name="New Group"))

def test_adv_modify_header(app):
    app.group.modify(Group(header="New_header"))
