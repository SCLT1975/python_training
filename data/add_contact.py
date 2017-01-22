from model.new_user_data import N_u_d
import random
import string


constant = [
            N_u_d(namef="namef1", namem="namem1", namel="namel1", nick="nick1", title="title1", firm="firm1",
                  addr="address1", phone_h="phoneh1", phone_m="phone_m", phone_work="phone_w", phone_fax="phone_fax1",
                  email_1="email11", email_2="email_2", email_3="email_3", homep="home_page",
                  day_1 = "//div[@id='content']/form/select[1]//option[3]",
                  month_1 = "//div[@id='content']/form/select[2]//option[2]", year_1="year",
                  day_2 = "//div[@id='content']/form/select[3]//option[3]",
                  month_2 = "//div[@id='content']/form/select[4]//option[2]",
                  year_2="year", address_2="address", phone_h2="phone_h2", notes="notes")
]


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
