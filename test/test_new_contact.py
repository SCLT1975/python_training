# -*- coding: utf-8 -*-

from model.new_user_data import N_u_d




def test_test_new_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.Create()
    app.contact.Fill_in(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=N_u_d.id_or_max) == sorted(new_contacts, key=N_u_d.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=N_u_d.id_or_max) == sorted(app.contact.get_contact_list(), key=N_u_d.id_or_max)





