# -*- coding: utf-8 -*-

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        print("Вспомогательный метод open_groups_page()")
        wd = self.app.wd
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

    def return_to_groups_page(self):
        print("Вспомогательный метод return_to_groups_page()")
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def select_first_group(self):
        print("Вспомогательный метод select_first_group()")
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()  # select first group

    def delete_first(self):
        print("Вспомогательный метод delete_first()")
        self.open_groups_page()
        wd = self.app.wd
        self.select_first_group()
        wd.find_element_by_name("delete").click()  # submit deletion
        self.return_to_groups_page()

    def modify_first(self, new_group_data):
        print("Вспомогательный метод modify_first()")
        self.open_groups_page()
        self.select_first_group()
        wd = self.app.wd
        wd.find_element_by_name("edit").click()  # open modification form
        self.fill_group_form(new_group_data)
        wd.find_element_by_name("update").click()  # submit modification
        self.return_to_groups_page()
