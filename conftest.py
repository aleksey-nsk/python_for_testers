# -*- coding: utf-8 -*-

import pytest

from fixture.application import Application


@pytest.fixture  # чтобы pytest догадался, что это не просто функция, а функция создающая фикстуру
def app(request):
    print("\n\n*********** Инициализатор фикстуры ***********")
    fixture = Application()  # создать фикстуру
    request.addfinalizer(fixture.destroy)  # pytest сам вызовет в нужный момент для разрушения фикстуры
    return fixture  # вернуть фикстуру
