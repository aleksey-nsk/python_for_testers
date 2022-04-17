# -*- coding: utf-8 -*-

from selenium import webdriver


class Application:
    # В конструкторе инициализация. Здесь запускаем браузер:
    def __init__(self):
        print("Конструктор класса Application")
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    # Вспомогательный метод для разрушения фикстуры. Здесь останавливаем браузер:
    def destroy(self):
        print("Вспомогательный метод destroy()")
        self.wd.quit()

    def open_home_page(self):
        print("Вспомогательный метод open_home_page()")
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def login(self, username, password):
        print("Вспомогательный метод login()")
        print("  username: " + username)
        print("  password: " + password)
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_groups_page(self):
        print("Вспомогательный метод open_groups_page()")
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def create_group(self, group):
        print("Вспомогательный метод create_group()")
        print("  group: " + str(group))
        wd = self.wd
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
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def logout(self):
        print("Вспомогательный метод logout()")
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()
