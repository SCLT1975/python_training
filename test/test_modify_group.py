from model.group import Group


def test_modify_1st_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(name="0000", header="Beauty", footer="of_the_dawn"))
    app.session.logout()
