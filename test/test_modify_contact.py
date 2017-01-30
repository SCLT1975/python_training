# -*- coding: utf-8 -*-

from model.new_user_data import N_u_d
import random


def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.Create()
        app.contact.Fill_in(N_u_d(namef="Rus", namem="Si", namel="An"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_info = N_u_d(namel= "Tree", namef= "Oak", namem="Great", nick="Alexander", title="Super boss", firm="0",
                    addr="Moscow", phone_h="0", phone_m="0", phone_work="0", phone_fax="0", email_2="0@vz.vz",
                    day_1 = "//div[@id='content']/form[1]/select[1]//option[9]",
                    month_2 = "//div[@id='content']/form[1]/select[4]//option[10]", address_2="0", phone_h2="0", id=contact.id)
    app.contact.modify_by_id(contact.id, contact_info)
    new_contacts = app.contact.get_contact_list()
    old_contacts.remove(contact)
    old_contacts.append(contact_info)
    assert sorted(old_contacts, key=N_u_d.id_or_max) == sorted(new_contacts, key=N_u_d.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=N_u_d.id_or_max) == sorted(app.contact.get_contact_list(), key=N_u_d.id_or_max)




