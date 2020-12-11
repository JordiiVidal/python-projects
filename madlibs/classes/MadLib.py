class MadLib:
    def __init__(self, category, title, text, blanks):
        self.category = category
        self.title = title
        self.text = text
        self.blanks = blanks
        self.result = text

    def generate(self):
        for blank in self.blanks:
            self.result = self.result.replace("_", blank.word, 1)
        return True

