from model.group import Group
import random


def test_adv_modify_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="251", header="578", footer="fhfkfh"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_data = Group(name="New Group", header="Pioneer", id=group.id)
    app.group.modify_by_id(group.id, group_data)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    old_groups.append(group_data)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

#    def test_adv_modify_name(app, db, check_ui):
#        if app.group.count() == 0:
#            app.group.create(Group(name="251", header="578", footer="fhfkfh"))
#        old_groups = db.get_group_list()
#        index = randrange(len(old_groups))
#        group = Group(name="New Group")
#        group.id = old_groups[index].id
#        app.group.modify_by_index(index, group)
#        new_groups = db.get_group_list()
#        old_groups[index] = group
#        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
#        if check_ui:
#            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

#def test_adv_modify_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="251", header="578", footer="fhfkfh"))
#    old_groups = app.group.get_group_list()
#    app.group.modify(Group(header="New_header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups)  == len(new_groups)
