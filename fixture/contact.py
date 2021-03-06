import logging.config
import re

from model.contact import Contact

logging.config.fileConfig('../log.conf')
log = logging.getLogger('simple')


class ContactHelper:
    contact_cache = None

    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        log.debug('Вспомогательный метод change_field_value()')
        log.debug('  field_name: ' + field_name)
        log.debug('  text: ' + text)
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def get_contact_list(self):
        log.debug('Вспомогательный метод get_contact_list()')

        if self.contact_cache is None:
            log.debug('  кэш пустой')
            self.app.navigation.open_home_page()
            self.contact_cache = []
            wd = self.app.wd
            for row in wd.find_elements_by_name('entry'):
                cells = row.find_elements_by_tag_name('td')
                firstname = cells[1].text
                lastname = cells[2].text
                id = cells[0].find_element_by_tag_name('input').get_attribute('value')
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname,
                                                  id=id, all_phones_from_home_page=all_phones))

        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        log.debug('Вспомогательный метод open_contact_to_edit_by_index()')
        log.debug('  index: ' + str(index))
        self.app.navigation.open_home_page()
        wd = self.app.wd
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name('a').click()

    def open_contact_view_by_index(self, index):
        log.debug('Вспомогательный метод open_contact_view_by_index()')
        log.debug('  index: ' + str(index))
        self.app.navigation.open_home_page()
        wd = self.app.wd
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    def get_contact_info_from_edit_page(self, index):
        log.debug('Вспомогательный метод get_contact_info_from_edit_page()')
        self.open_contact_to_edit_by_index(index)
        wd = self.app.wd
        wd.find_element_by_name('home')
        firstname = wd.find_element_by_name('firstname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')
        homephone = wd.find_element_by_name('home').get_attribute('value')
        workphone = wd.find_element_by_name('work').get_attribute('value')
        mobilephone = wd.find_element_by_name('mobile').get_attribute('value')
        secondaryphone = wd.find_element_by_name('phone2').get_attribute('value')
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone)

    def get_contact_from_view_page(self, index):
        log.debug('Вспомогательный метод get_contact_from_view_page()')
        self.open_contact_view_by_index(index)
        wd = self.app.wd
        text = wd.find_element_by_id('content').text
        homephone = re.search('H: (.*)', text).group(1)
        workphone = re.search('W: (.*)', text).group(1)
        mobilephone = re.search('M: (.*)', text).group(1)
        secondaryphone = re.search('P: (.*)', text).group(1)
        return Contact(homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone)
