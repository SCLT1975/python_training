import re


def test_contact_data(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.namef == contact_from_edit_page.namef
    assert contact_from_home_page.namel == contact_from_edit_page.namel
    assert contact_from_home_page.addr == contact_from_edit_page.addr
    assert contact_from_home_page.all_email == merge_email_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(N_u_d):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [N_u_d.phone_h, N_u_d.phone_m, N_u_d.phone_work, N_u_d.phone_h2]))))


def merge_email_like_on_home_page(N_u_d):
    return "\n".join(filter(lambda x: x != "",
                     (filter(lambda x: x is not None,
                             [N_u_d.email_1, N_u_d.email_2, N_u_d.email_3]))))
