# -*- coding: utf-8 -*-
from model.new_user_data import N_u_d
import random

def test_new_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.Create()
        app.contact.Fill_in(N_u_d(namef="Rus", namem="Si", namel="An"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert sorted(old_contacts, key=N_u_d.id_or_max) == sorted(new_contacts, key=N_u_d.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=N_u_d.id_or_max) == sorted(app.contact.get_contact_list(), key=N_u_d.id_or_max)

