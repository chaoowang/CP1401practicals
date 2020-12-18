class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflaction=False, year=0):
        self.name=name
        self.typing=typing
        self.reflaction=reflaction
        self.year=year

    def __str__(self):
        return ("{}, typing: {}, reflection: {}, First appeared in {}".format(self.name, self.typing, self.reflaction, self.year))

    def is_dynamic(self):
        return self.typing == "Dynamic"