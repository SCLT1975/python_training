# -*- coding: utf-8 -*-

from model.new_user_data import N_u_d


def test_modify_contact(app):
    app.contact.Create()
    app.contact.modify_1st(N_u_d(namem="Great",  nick="Alexander", title="Super boss", firm="0", addr="Moscow", phone_h="0", phone_m="0",
                                   phone_work="0", phone_fax="0",  email_2="0@vz.vz", day_1 = "//div[@id='content']/form[1]/select[1]//option[9]", month_2 = "//div[@id='content']/form[1]/select[4]//option[10]", address_2="0",
                                   address_3="0", ))




