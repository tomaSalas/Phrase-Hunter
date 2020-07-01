class Character:
    def __init__(self, a_character, was_guessed=False):
        self.a_character = a_character
        self.was_guessed = was_guessed

    def compare(self, a_string):
        if self.a_character == " ":
            self.was_guessed = True
        elif self.was_guessed:
            pass
        elif a_string == self.a_character:
            self.was_guessed = True
        else:
            self.was_guessed = False

    def reset_word(self):
        if self.was_guessed == True:
            self.was_guessed = False
