# -*- coding: utf-8 -*-

import pytest

from fixture.application import Application

fixture = None


@pytest.fixture  # чтобы pytest догадался, что это не просто функция, а функция создающая фикстуру
def app(request):
    print("\n\n**************** Фикстура app ****************")
    global fixture  # будем использовать данную глобальную переменную
    browser = request.config.getoption('--browser')
    base_url = request.config.getoption('--baseUrl')

    if fixture is None:
        fixture = Application(browser, base_url)  # создать фикстуру
    else:
        if not fixture.is_valid():
            fixture = Application(browser, base_url)

    fixture.session.ensure_login(username="admin", password="secret")
    return fixture  # вернуть фикстуру


# Для финализации делаем отдельную фикстуру:
#   scope="session" => значит фикстура будет создаваться одна на всю сессию (на весь сеанс запуска тестов).
#   autouse=True => фикстура сработает автоматически, даже не смотря на то, что она ни в каком тесте явно не указана.
@pytest.fixture(scope="session", autouse=True)
def stop(request):
    print("\n\n**************** Фикстура stop ***************")

    def fin():
        print("\n\nВспомогательный метод fin(). Вызывается при разрушении фикстуры !!!")
        fixture.session.ensure_logout()
        fixture.stop_browser()

    request.addfinalizer(fin)  # pytest сам вызовет в нужный момент метод addfinalizer() для разрушения фикстуры
    return fixture  # вернуть фикстуру


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--baseUrl', action='store', default='http://localhost/addressbook/')
