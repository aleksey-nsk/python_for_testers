# -*- coding: utf-8 -*-

from model.group import Group


class GroupHelper:
    group_cache = None

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        print("Вспомогательный метод open_groups_page()")
        print("  current_url:", wd.current_url)
        # Если условие не выполняется, тогда сделать клик по ссылке:
        if not (wd.current_url.endswith('/group.php') and len(wd.find_elements_by_name('new')) > 0):
            print("  сделать клик по ссылке")
            wd.find_element_by_link_text("groups").click()

    def change_field_value(self, field_name, text):
        print("Вспомогательный метод change_field_value()")
        print("  field_name: " + field_name)
        print("  text:", text)
        wd = self.app.wd
        if text is not None:
            print("  Заполнить поле")
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_group_form(self, group):
        print("Вспомогательный метод fill_group_form()")
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def create(self, group):
        print("Вспомогательный метод create()")
        print("  group: " + str(group))
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()  # init group creation
        self.fill_group_form(group)
        wd.find_element_by_name("submit").click()  # submit group creation
        self.return_to_groups_page()
        self.group_cache = None

    def return_to_groups_page(self):
        print("Вспомогательный метод return_to_groups_page()")
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def select_first_group(self):
        print('Вспомогательный метод select_first_group()')
        self.select_group_by_index(0)

    def select_group_by_index(self, index):
        print('Вспомогательный метод select_group_by_index()')
        print('  index:', index)
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first(self):
        print('Вспомогательный метод delete_first()')
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        print('Вспомогательный метод delete_group_by_index()')
        self.open_groups_page()
        self.select_group_by_index(index)
        wd = self.app.wd
        wd.find_element_by_name('delete').click()  # submit deletion
        self.return_to_groups_page()
        self.group_cache = None

    def modify_first(self, new_group_data):
        print('Вспомогательный метод modify_first()')
        self.modify_group_by_index(0, new_group_data)

    def modify_group_by_index(self, index, new_group_data):
        print('Вспомогательный метод modify_group_by_index()')
        self.open_groups_page()
        self.select_group_by_index(index)
        wd = self.app.wd
        wd.find_element_by_name("edit").click()  # open modification form
        self.fill_group_form(new_group_data)
        wd.find_element_by_name("update").click()  # submit modification
        self.return_to_groups_page()
        self.group_cache = None

    def count(self):
        print("Вспомогательный метод count()")
        self.open_groups_page()
        wd = self.app.wd
        group_count = len(wd.find_elements_by_name("selected[]"))
        print("  количество групп в адресной книге: " + str(group_count))
        return group_count

    def get_group_list(self):
        print('Вспомогательный метод get_group_list()')

        if self.group_cache is None:
            print('  кэш пустой')
            self.open_groups_page()
            wd = self.app.wd
            self.group_cache = []
            for element in wd.find_elements_by_css_selector('span.group'):
                text = element.text
                id = element.find_element_by_name('selected[]').get_attribute('value')
                self.group_cache.append(Group(name=text, id=id))

        return list(self.group_cache)
