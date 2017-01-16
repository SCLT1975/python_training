# -*- coding: utf-8 -*-
from model.new_user_data import N_u_d


def test_new_contact(app):
    if app.contact.count() == 0:
        app.contact.Create()
        app.contact.Fill_in(N_u_d(namef="Rus", namem="Si", namel="An"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_1st()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
