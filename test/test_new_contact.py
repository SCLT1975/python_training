# -*- coding: utf-8 -*-

from model.new_user_data import N_u_d
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*20
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])

testdata = [
            N_u_d(namef=random_string("namef", 10), namem=random_string("namem", 10), namel=random_string("namel", 10),
                  nick=random_string("nick", 6), title=random_string("title", 9), firm=random_string("firm", 12),
                  addr=random_string("address", 20), phone_h=random_string("phoneh", 7),
                  phone_m=random_string("phone_m", 7), phone_work=random_string("phone_w", 7),
                  phone_fax=random_string("phone_fax", 7), email_1=random_string("email1", 7),
                  email_2=random_string("email_2", 10), email_3=random_string("email_3", 10),
                  homep=random_string("home_page", 12), day_1 = "//div[@id='content']/form/select[1]//option[3]",
                  month_1 = "//div[@id='content']/form/select[2]//option[2]", year_1 = random_string("year", 6),
                  day_2 = "//div[@id='content']/form/select[3]//option[3]",
                  month_2 = "//div[@id='content']/form/select[4]//option[2]",
                  year_2 = random_string("year", 6), address_2=random_string("address", 15),
                  phone_h2=random_string("phone_h2", 6), notes=random_string("notes", 20))
            for i in range(5)
]



@pytest.mark.parametrize("contact", testdata, ids = [repr(x) for x in testdata])
def test_test_new_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.Create()
    app.contact.Fill_in(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=N_u_d.id_or_max) == sorted(new_contacts, key=N_u_d.id_or_max)





