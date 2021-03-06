from sys import maxsize


class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __str__(self):
        result = "Group"
        if self.name:
            result += "{name='" + self.name + "'}"
        if self.header:
            result += "{header='" + self.header + "'}"
        if self.footer:
            result += "{footer='" + self.footer + "'}"
        if self.id:
            result += "{id='" + self.id + "'}"
        return result

    def __repr__(self):
        return '%s: %s, %s, %s' % (self.id, self.name, self.header, self.footer)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
