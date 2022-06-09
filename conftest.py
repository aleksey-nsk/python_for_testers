# -*- coding: utf-8 -*-

import json

import pytest

from fixture.application import Application

target = None
fixture = None


@pytest.fixture  # чтобы pytest догадался, что это не просто функция, а функция создающая фикстуру
def app(request):
    print("\n\n**************** Фикстура app ****************")

    # Будем использовать данные глобальные переменные
    global target
    global fixture

    browser = request.config.getoption('--browser')

    if target is None:
        with open(request.config.getoption('--target')) as config_file:
            target = json.load(config_file)

    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target['baseUrl'])  # создать фикстуру

    fixture.session.ensure_login(username=target['username'], password=target['password'])
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
    parser.addoption('--target', action='store', default='target.json')
