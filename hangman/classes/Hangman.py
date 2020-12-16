class Hangman:
    def __init__(self, word):
        self.word = word.upper()
        self.state = self.create_state(word)
        self.used_letters = []

    @staticmethod  # return ____ with a length of a word
    def create_state(word):
        state = ""
        for x in range(len(word)):
            state += "_"
        return state

    def win(self):
        if self.word == self.state:
            return True
        return False

    def check_letter(self, letter):
        self.add_letter(letter)
        for index in range(len(self.word)):
            if letter.upper() == self.word[index]:
                new_state = list(self.state)
                new_state[index] = letter.upper()
                self.state = "".join(new_state)

    def add_letter(self, letter):
        if letter not in self.used_letters:
            self.used_letters.append(letter)
