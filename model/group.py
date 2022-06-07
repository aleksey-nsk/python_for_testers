class Group:
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __str__(self):
        # return "Group{name='" + self.name + "', header='" + self.header + "', footer='" + self.footer + "'}"
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
        return '%s:%s' % (self.id, self.name)

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name
