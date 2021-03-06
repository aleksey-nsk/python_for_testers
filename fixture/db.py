import logging.config

import mysql.connector

from model.group import Group

logging.config.fileConfig('../log.conf')
log = logging.getLogger('simple')


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def destroy(self):
        self.connection.close()

    def get_group_list(self):
        log.debug('Загрузка списка групп из БД')
        list = []
        cursor = self.connection.cursor()

        try:
            sql = 'select group_id, group_name, group_header, group_footer from group_list'
            cursor.execute(sql)
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()

        return list
