import re

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)



def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.phone_h == contact_from_edit_page.phone_h
    assert contact_from_view_page.phone_work == contact_from_edit_page.phone_work
    assert contact_from_view_page.phone_m == contact_from_edit_page.phone_m
    assert contact_from_view_page.phone_h2 == contact_from_edit_page.phone_h2


def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(N_u_d):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [N_u_d.phone_h, N_u_d.phone_m, N_u_d.phone_work, N_u_d.phone_h2]))))
