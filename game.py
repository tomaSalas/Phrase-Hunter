from character import Character
from phrase import Phrase
import random
import sys
import re

attempts = []
game_phrases = ["skyrim",
                "deadspace",
                "the last of us",
                "resident evil",
                "neon genesis evangelion"]


class Game():
    def __init__(self, phrase, lives=5, game_not_over=True):
        self.phrase = Phrase(phrase)
        self.lives = lives
        self.game_not_over = game_not_over
        self.factor = lives

    def star_game(self):
        self.intro()
        while self.game_not_over:
            self.save_attempt(self.check_input())
            print("attempt(s): " + ", ".join(attempts) + "\n")
            self.iterate_attempts()
            self.phrase.show()
            self.end(self.phrase.correct_phrase())
            self.incorrect_letter(self.iterate_attempts_incorrect())

    def intro(self):
        print(("*" * 65))
        print(("-" * 15) + " Welcome to the Pharse Hunter Game " + ("-" * 15))
        print(("-" * 22) + " made by Tomas Salas " + ("-" * 22))
        print(("*" * 65) + "\n")
        self.hidden_phrase()

    def goodbye(self):
        print("Thank you for playing!")

    def hidden_phrase(self):
        self.phrase
        self.phrase.iterate(None)
        self.phrase.show()

    def check_input(self):
        while True:
            count = 0
            count_letter = 0
            print("\n")
            letter = input("Guess a letter:   ")
            for char in letter:
                count_letter += 1
            if count_letter == 1:
                check = bool(re.search(r'[^a-zA-Z]', letter))
                if check == False:
                    return letter
                else:
                    print("Oh no! that is not a valid character. Please try again")
                    continue
            else:
                print("Oh no! that is more than a letter. Please try again")
                continue

    def save_attempt(self, letter):
        attempts.append(letter)

    def iterate_attempts(self):
        for attempt in attempts:
            self.phrase.iterate(attempt)

    def iterate_attempts_incorrect(self):
        save_result = self.phrase.incorrect_character(attempts[-1])
        return save_result

    def incorrect_letter(self, stringg):
        if stringg == True:
            print("You got that letter right! 💁")
        else:
            self.factor -= 1
            print("Oh no! You got {} lives out of {}".format(self.factor, self.lives)+ " 🙈")
            if self.factor == 0:
                print("You lost! Better luck next time 😉")
                self.end(True)

    def end(self, booll):
        while booll:
            print("Would you like to try again? Type either \'YES\' or \'NO\'")
            answer = input(">    ")
            if answer.upper() == "YES":
                self.clear_attempts()
                self.phrase.phrase_reset_status()
                self.phrase.phrase_reset()
                game = Game(self.ramdon_phrase())
                game.star_game()
                sys.exit()
            elif answer.upper() == "NO":
                self.goodbye()
                sys.exit()
            else:
                print("Oh no! That is not a valid input. Type either \'YES\' or \'NO\' ")

    def ramdon_phrase(self):
        ph = game_phrases[random.randint(0, (len(game_phrases) - 1))]
        return ph

    def clear_attempts(self):
        attempts.clear()
