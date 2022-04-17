# -*- coding: utf-8 -*-

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        print("Вспомогательный метод open_groups_page()")
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        print("Вспомогательный метод create()")
        print("  group: " + str(group))
        wd = self.app.wd
        self.open_groups_page()
        # Init group creation:
        wd.find_element_by_name("new").click()
        # Fill group form:
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Submit group creation:
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        print("Вспомогательный метод return_to_groups_page()")
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
