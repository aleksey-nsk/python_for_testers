# Info
- Примеры автотестов на Python

### 1. Подготовка инфраструктуры. Основы программирования на Python
- Интерпретатор Python:  
`python --version` => **Python 3.8.10**

- Менеджер пакетов pip:  
`pip --version` => **pip 21.1.1**

- **IPython** - улучшенная интерактивная консоль:  
`ipython --version` => **8.2.0**  
`ipython` => зайти в IPython  
`exit()` => выйти  

- Среда разработки **PyCharm 2021.3.3 Community Edition**

- Хранилище пакетов **PyPI** (сайт https://pypi.org/)

- Тестовый фреймворк **pytest**

- Директория `venv` в корне проекта - это **виртуальное окружение Python** (в репозиторий не сохранять!)

- Основы программирования на Python: переменные и значения, типы данных, операции и выражения с простыми типами,
функции, библиотеки и import, классы и объекты, модули и пакеты.

- Написал первый браузерный автотест: **Katalon Recorder 5.5.3** -> Export -> Python (WebDriver + unittest)  
`pip install selenium==3.12.0` (команду см. на https://pypi.org/)

- Установил тестовый фреймворк **pytest** вместо стандартного **unittest**  
`pip install pytest==3.7.1`

- Вспомогательный исполняемый файл для Firefox:  
Скачать **geckodriver-v0.31.0-win64.zip** -> разархивировать и сам файл **geckodriver.exe**
положить в **C:\Windows\System32**

- Запустить тесты в консоли:

Активировать виртуальное окружение в командной строке Windows:  
`C:\Users\alexw\Desktop\_MY_FILES\My_documents\work_projects\python_for_testers>venv\Scripts\activate`

Запустить все тесты из файла test_add_group.py командой:  
`(venv) C:\Users\alexw\Desktop\_MY_FILES\My_documents\work_projects\python_for_testers>py.test test\test_add_group.py`

- Выделил вспомогательные функции

- Добавил **параметры** в методы

- Выделил вспомогательные классы

### 2. Двухуровневая архитектура тестового набора
- Стек автотестирования

- **Фикстуры PyTest** - функции, запускаемые *до* и *после* теста.

- **Декомпозиция** сложных классов:  
Декомпозировал класс Application: выделил **классы-хелперы**: SessionHelper, GroupHelper, NavigationHelper

- Как сделать функцию, которая создаёт фикстуру, общей для всех тестов? Решение pytest: поместить фикстуру
в файл **conftest.py** (положить в корень проекта) => в итоге фикстура стала общей, и ею можно пользоваться
в любой тестовой функции.

- Как использовать один и тот же браузер для запуска всех тестов? Решение:

`@pytest.fixture(scope="session")`

**scope="session"** => теперь фикстура будет создаваться одна на всю сессию (на весь сеанс запуска тестов),
а не для каждого отдельного теста. Теперь тесты работают быстрее, т.к. не тратится время на запуск новых
экземпляров браузера.

### 3. Управление потоком выполнения кода - условный переход
- Проверка условий `if`
 
- Интеллектуальная фикстура. Тут обработка исключения `try-except`

### Примеры автотестов на REST API
- пакет `test_rest_api_DataEast`

- тестовый фреймворк **pytest**

- библиотека для HTTP-запросов **requests 2.23.0**

- примеры тут:  
![](https://github.com/cont-azhdanov/python_for_testers/blob/master/screenshots/01_package_with_rest_api_tests.png)  
Проверка эндпоинтов: **Enrich**, **StandardGeographyQuery**, **DataLayers**, **Countries**.

- Для запросов на GeoEnrichmentServer необходимо сформировать **API key** в личном кабинете
на сайте **ArcGIS Developer**:  
![](https://github.com/cont-azhdanov/python_for_testers/blob/master/screenshots/02_arcgis_key.png)  

Далее в корне проекта создать директрию `token`, а внутри неё файл `congif.ini`:  
![](https://github.com/cont-azhdanov/python_for_testers/blob/master/screenshots/03_token_dir.png)  

В файле `congif.ini` создать раздел `[Settings]` и в нём параметр `token`. Вставить сюда свой **API key**:  
![](https://github.com/cont-azhdanov/python_for_testers/blob/master/screenshots/04_config_file.png)  
