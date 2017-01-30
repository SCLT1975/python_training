import mysql.connector
from model.group import Group
from model.new_user_data import N_u_d

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host = host, database = name, user = user, password = password)
        self.connection.autocommit = True


    def destroy(self):
        self.connection.close()

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name = name, header = header, footer = footer))
        finally:
            cursor.close()
        return list


    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address from addressbook")
            for row in cursor:
                (id, firstname, lastname, address) = row
                list.append(N_u_d(id=str(id), namef = firstname, namel= lastname, addr = address))
        finally:
            cursor.close()
        return list
