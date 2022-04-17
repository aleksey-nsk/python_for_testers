class Group:
    def __init__(self, name, header, footer):
        self.name = name
        self.header = header
        self.footer = footer

    def __str__(self):
        return "Group{name='" + self.name + "', header='" + self.header + "', footer='" + self.footer + "'}"
