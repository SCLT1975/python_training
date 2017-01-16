# -*- coding: utf-8 -*-
from model.new_user_data import  N_u_d

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def select_1st_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()



    def Create(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()


    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_field_value2(self, choise1):
        wd = self.app.wd
        if choise1 is not None:
            wd.find_element_by_xpath(choise1).click()

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    def delete_1st(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        # open contact page
        self.open_contact_page()
        #choose&delete
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def modify_1st(self):
        self.modify_by_index(0)

    def modify_by_index(self, index, N_u_d):
        wd = self.app.wd
        # open contact page
        self.open_contact_page()
        # choose&edit
        self.open_contact_to_edit_by_index(index)
        self.change_field_value("firstname",N_u_d.namef)
        self.change_field_value("middlename", N_u_d.namem)
        self.change_field_value("lastname", N_u_d.namel)
        self.change_field_value("nickname", N_u_d.nick)
        self.change_field_value("title", N_u_d.title)
        self.change_field_value("company", N_u_d.firm)
        self.change_field_value("address", N_u_d.addr)
        self.change_field_value("home", N_u_d.phone_h)
        self.change_field_value("mobile", N_u_d.phone_m)
        self.change_field_value("work", N_u_d.phone_work)
        self.change_field_value("fax", N_u_d.phone_fax)
        self.change_field_value("email", N_u_d.email_1)
        self.change_field_value("email2", N_u_d.email_2)
        self.change_field_value("email3", N_u_d.email_3)
        self.change_field_value("homepage", N_u_d.homep)
        self.change_field_value2(N_u_d.day_1)
        self.change_field_value2(N_u_d.month_1)
        self.change_field_value("byear", N_u_d.year_1)
        self.change_field_value2(N_u_d.day_2)
        self.change_field_value2(N_u_d.month_2)
        self.change_field_value("ayear", N_u_d.year_2)
        self.change_field_value("address2", N_u_d.address_2)
        self.change_field_value("phone2", N_u_d.address_3)
        self.change_field_value("notes", N_u_d.notes)
        wd.find_element_by_name("update").click()
        self.contact_cache = None


    def Fill_in(self, N_u_d):
        wd = self.app.wd
        self.change_field_value("firstname", N_u_d.namef)
        self.change_field_value("middlename", N_u_d.namem)
        self.change_field_value("lastname", N_u_d.namel)
        self.change_field_value("nickname", N_u_d.nick)
        self.change_field_value("title", N_u_d.title)
        self.change_field_value("company", N_u_d.firm)
        self.change_field_value("address", N_u_d.addr)
        self.change_field_value("home", N_u_d.phone_h)
        self.change_field_value("mobile", N_u_d.phone_m)
        self.change_field_value("work", N_u_d.phone_work)
        self.change_field_value("fax", N_u_d.phone_fax)
        self.change_field_value("email", N_u_d.email_1)
        self.change_field_value("email2", N_u_d.email_2)
        self.change_field_value("email3", N_u_d.email_3)
        self.change_field_value("homepage", N_u_d.homep)
        self.change_field_value2(N_u_d.day_1)
        self.change_field_value2(N_u_d.month_1)
        self.change_field_value("byear", N_u_d.year_1)
        self.change_field_value2(N_u_d.day_2)
        self.change_field_value2(N_u_d.month_2)
        self.change_field_value("ayear", N_u_d.year_2)
        self.change_field_value("address2", N_u_d.address_2)
        self.change_field_value("phone2", N_u_d.address_3)
        self.change_field_value("notes", N_u_d.notes)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_css_selector("td")
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                namef = cells[2].text
                namel = cells[1].text
                self.contact_cache.append(N_u_d(namef=namef, namel=namel, id=id))
        return list(self.contact_cache)

