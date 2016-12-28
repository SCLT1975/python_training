# -*- coding: utf-8 -*-

from model.new_user_data import N_u_d


def test_modify_contact(app):
    app.contact.Create()
    app.contact.modify_1st(N_u_d(namef="0", namem="0", namel="0", nick="0", title="0", firm="0", addr="0-York", phone_h="0", phone_m="0",
                                   phone_work="0", phone_fax="0", email_1="0@pp.pp", email_2="0@vz.vz", email_3="0@ya.ya", homep="0.ya.ya", address_2="0",
                                   address_3="0", notes="0"))




