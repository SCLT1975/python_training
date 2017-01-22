# -*- coding: utf-8 -*-

from model.new_user_data import N_u_d




def test_test_new_contact(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.Create()
    app.contact.Fill_in(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=N_u_d.id_or_max) == sorted(new_contacts, key=N_u_d.id_or_max)





