# -*- coding: utf-8 -*-

from model.new_user_data import N_u_d


def test_test_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.Create()
    app.contact.Fill_in(N_u_d(namef="Vas", namem="Sav", namel="pioneer", nick="LG", title="boss", firm="YA", addr="New-York", phone_h="2312", phone_m="56456",
                                   phone_work="423433223", phone_fax="6456456", email_1="pp@pp.pp", email_2="vz@vz.vz", email_3="ya@ya.ya", homep="www.ya.ya", day_1 = "//div[@id='content']/form/select[1]//option[3]", month_1 = "//div[@id='content']/form/select[2]//option[2]", year_1 = "1917",  day_2 = "//div[@id='content']/form/select[3]//option[3]", month_2 = "//div[@id='content']/form/select[4]//option[2]", year_2 = "1991",  address_2="dfasdfasf",
                                   address_3="asdfasfrt", notes="jrkyuyrrjrt"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)




