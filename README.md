# Info
- Проект **Автотесты**
- Тестируемое приложение **адресная книга**: для установки используется **готовая сборка XAMPP**
- Для тестирования **REST API** используется **GeoEnrichmentServer** у приложения **ArcGIS**

### Используемые инструменты
- Версия интерпретатор **Python 3.8.10**
- Менеджер пакетов **pip 21.1.1**
- Среда разработки **PyCharm 2021.3.3 Community Edition**
- Тестовый фреймворк **pytest 3.7.1**
- Библиотека **selenium 3.12.0**
- Вспомогательный исполняемый файл для Firefox **geckodriver.exe** положить в **C:\Windows\System32**
- Библиотека **requests 2.18.4** для HTTP-запросов
- Библиотека **jsonpickle 2.2.0** для преобразования объектов Python в формат **JSON** и обратно
- Модуль **logging** для логирования
- Модуль **configparser** для парсера конфигурации
- Полный список зависимостей находится в файле **requirements.txt**

### Файлы и папки в корневой директории проекта
- `директория test` содержит сами тесты
- `директория model` содержит классы сущностей Группа и Контакт
- `директория generator` содержит генератор тестовых данных. Сами данные записываются в `директорию data`
- `директория fixture` для класса **Application** и вспомогательных **классов-хелперов**
- `директория data` для тестовых данных
- `файл conftest.py` содержит список всех **фикстур**
- `файл log.conf` описывает настройки логирования
- `файл target.json` содержит базовые настройки тестируемого приложения
- `файл requirements.txt` содержит полный список зависимостей

### Тестирование REST API
Для запросов на GeoEnrichmentServer необходимо сформировать **API key** в личном кабинете
на сайте **ArcGIS Developer**:  
![](https://github.com/aleksey-nsk/python_for_testers/blob/master/screenshots/02_arcgis_key.png)  

Далее в корне проекта создать директрию `token`, а внутри неё файл `congif.ini`:  
![](https://github.com/aleksey-nsk/python_for_testers/blob/master/screenshots/03_token_dir.png)  

В файле `congif.ini` создать раздел `[Settings]` и в нём параметр `token`. Вставить сюда свой **API key**:  
![](https://github.com/aleksey-nsk/python_for_testers/blob/master/screenshots/04_config_file.png)  
