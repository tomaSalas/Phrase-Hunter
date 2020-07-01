from character import Character

char_list1 = []
char_list2 = []


class Phrase:
    def __init__(self, phrase):
        for char in phrase:
            char_list1.append(Character(char))
        self.phrase = char_list1

    def iterate(self, a_string):
        """evaluates every string pass
           to Character.a_character
           """
        for char in self.phrase:
            char.compare(a_string)

    def correct_phrase(self):
        """when all characters in phrase == true
            return True
            """
        count = 0
        for char in self.phrase:
            if char.was_guessed == True:
                count += 1
        if count == len(char_list1):
            print("You match all the characters!")
            return True
        else:
            return False

    def incorrect_character(self, a_string):
        """if one character in phrase == a_string
            return false
            """
        index = 0
        while True:
            test = self.phrase[index]
            if test.a_character == a_string:
                return True
            elif index == (len(self.phrase) - 1):
                return False
            else:
                index += 1

    def all_correct(self):
        for char in self.phrase:
            char.was_guessed = True

    def show(self):
        for char in self.phrase:
            if char.was_guessed == True:
                char_list2.append(char.a_character)
            else:
                char_list2.append("_")
        print(" ".join(char_list2))
        char_list2.clear()

    def phrase_reset_status(self):
        for char in self.phrase:
            char.reset_word()

    def phrase_reset(self):
        char_list1.clear()
