# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application
from model.new_user_data import N_u_d


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture




def test_test_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.Create()
    app.contact.Fill_in(N_u_d(namef="Vas", namem="Sav", namel="pioneer", nick="LG", title="boss", firm="YA", addr="New-York", phone_h="2312", phone_m="56456",
                                   phone_work="423433223", phone_fax="6456456", email_1="pp@pp.pp", email_2="vz@vz.vz", email_3="ya@ya.ya", homep="www.ya.ya", address_2="dfasdfasf",
                                   address_3="asdfasfrt", notes="jrkyuyrrjrt"))
    app.session.logout()



