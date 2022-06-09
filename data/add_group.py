import random
import string

from model.group import Group

constant = [
    Group(name='name1', header='header1', footer='footer1'),
    Group(name='name2', header='header2', footer='footer2')
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    random_str = prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    return random_str


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string('name_', 10), header=random_string('header_', 5), footer=random_string('footer_', 5))
    for i in range(3)
]
