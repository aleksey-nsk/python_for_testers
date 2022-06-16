# -*- coding: utf-8 -*-

import importlib
import json
import logging.config
import os

import jsonpickle
import pytest

from fixture.application import Application
from fixture.db import DbFixture

logging.config.fileConfig('../log.conf')
log = logging.getLogger('simple')

target = None
fixture = None


def load_config(file):
    global target

    if target is None:
        abs_path = os.path.abspath(__file__)
        dir_name = os.path.dirname(abs_path)
        config_file = os.path.join(dir_name, file)
        with open(config_file) as f:
            target = json.load(f)

    return target


@pytest.fixture  # чтобы pytest догадался, что это не просто функция, а функция создающая фикстуру
def app(request):
    log.debug("**************** Фикстура app ****************")
    global fixture  # будем использовать данную глобальную переменную
    browser = request.config.getoption('--browser')
    web_config = load_config(request.config.getoption('--target'))['web']

    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])  # создать фикстуру

    fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
    return fixture  # вернуть фикстуру


@pytest.fixture(scope='session')
def db(request):
    log.debug("***************** Фикстура db ****************")
    db_config = load_config(request.config.getoption('--target'))['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'],
                          user=db_config['user'], password=db_config['password'])

    def fin():
        dbfixture.destroy()

    request.addfinalizer(fin)
    return dbfixture


@pytest.fixture
def check_ui(request):
    log.debug("************** Фикстура check_ui *************")
    check = request.config.getoption('--check_ui')
    log.debug("check: " + str(check))
    return check


# Для финализации делаем отдельную фикстуру:
#   scope="session" => значит фикстура будет создаваться одна на всю сессию (на весь сеанс запуска тестов).
#   autouse=True => фикстура сработает автоматически, даже не смотря на то, что она ни в каком тесте явно не указана.
@pytest.fixture(scope="session", autouse=True)
def stop(request):
    log.debug("**************** Фикстура stop ***************")

    def fin():
        log.debug("Вспомогательный метод fin(). Вызывается при разрушении фикстуры !!!")
        if fixture is not None:
            fixture.session.ensure_logout()
            fixture.stop_browser()

    request.addfinalizer(fin)  # pytest сам вызовет в нужный момент метод addfinalizer() для разрушения фикстуры
    return fixture  # вернуть фикстуру


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--target', action='store', default='target.json')
    parser.addoption('--check_ui', action='store_true')


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
