from sys import maxsize

class N_u_d:
    def __init__(self, namef = None, namem = None, namel = None, nick = None, title = None, firm = None, addr = None,
                 phone_h = None, phone_m = None, phone_work = None, phone_fax = None, email_1 = None, email_2 = None,
                 email_3 = None, homep = None, day_1 = None, month_1 = None, year_1 = None, day_2 = None,
                 month_2 = None, year_2 = None, address_2 = None, phone_h2 = None, notes = None, id = None,
                 all_phones_from_home_page = None, all_email = None):
        self.namef = namef
        self.namem = namem
        self.namel = namel
        self.nick = nick
        self.title = title
        self.firm = firm
        self.addr = addr
        self.phone_h = phone_h
        self.phone_m = phone_m
        self.phone_work = phone_work
        self.phone_fax = phone_fax
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.homep = homep
        self.day_1 = day_1
        self.month_1 = month_1
        self.year_1 = year_1
        self.day_2 = day_2
        self.month_2 = month_2
        self.year_2 = year_2
        self.address_2 = address_2
        self.phone_h2 = phone_h2
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_email = all_email


    def __repr__(self):
        return "%s:%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s" % (self.id, self.namef, self.namel,
                                                                                self.nick, self.title, self.firm, self.addr,
                                                                                self.phone_h, self.phone_m, self.phone_work,
                                                                                self.phone_fax, self.email_1,self.email_2,
                                                                                self.email_3, self.homep, self.year_1, self.year_2,
                                                                                self.address_2, self.phone_h2, self.notes)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.namef == other.namef \
               and self.namel == other.namel and self.addr == other.addr


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize