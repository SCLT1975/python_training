# -*- coding: utf-8 -*-

from model.new_user_data import N_u_d


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.Create()
        app.contact.Fill_in(N_u_d(namef="Rus", namem="Si", namel="An"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_1st(N_u_d(namem="Great",  nick="Alexander", title="Super boss", firm="0", addr="Moscow", phone_h="0", phone_m="0",
                                   phone_work="0", phone_fax="0",  email_2="0@vz.vz", day_1 = "//div[@id='content']/form[1]/select[1]//option[9]", month_2 = "//div[@id='content']/form[1]/select[4]//option[10]", address_2="0",
                                   address_3="0", ))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)




