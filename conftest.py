# -*- coding: utf-8 -*-

import importlib
import json
import os

import jsonpickle
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
        abs_path = os.path.abspath(__file__)  # абсолютный путь к текущему файлу
        dir_name = os.path.dirname(abs_path)  # директория, в которой лежит текущий файл
        config_file = os.path.join(dir_name, request.config.getoption('--target'))  # абсолютный путь к конфигу
        with open(config_file) as f:
            target = json.load(f)

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


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith('data_'):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith('json_'):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module('data.%s' % module).testdata


def load_from_json(file):
    abs_path = os.path.abspath(__file__)
    dir_name = os.path.dirname(abs_path)
    with open(os.path.join(dir_name, 'data/%s.json' % file)) as f:
        return jsonpickle.decode(f.read())
