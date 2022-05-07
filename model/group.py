class Group:
    def __init__(self, name=None, header=None, footer=None):
        self.name = name
        self.header = header
        self.footer = footer

    def __str__(self):
        # return "Group{name='" + self.name + "', header='" + self.header + "', footer='" + self.footer + "'}"
        result = "Group"
        if self.name:
            result += "{name='" + self.name + "'}"
        if self.header:
            result += "{header='" + self.header + "'}"
        if self.footer:
            result += "{footer='" + self.footer + "'}"
        return result
