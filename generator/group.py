import json
import os
import random
import string

from model.group import Group


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    random_str = prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    return random_str


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string('name_', 10), header=random_string('header_', 5), footer=random_string('footer_', 5))
    for i in range(3)
]

# Сохранить сгенерированные данные в файл
abs_path = os.path.abspath(__file__)
dir_name = os.path.dirname(abs_path)
file = os.path.join(dir_name, '../data/groups.json')
with open(file, 'w') as f:
    f.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=4))
