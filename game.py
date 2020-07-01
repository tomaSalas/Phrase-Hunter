from character import Character
from phrase import Phrase
import random
import sys
import re


class Game():
    def __init__(self, phrases, lives=5, game_not_over=True):
        self.raw_phrases = phrases
        self.phrases = [phrase for phrase in phrases]
        self.phrase = Phrase(
            self.phrases[random.randint(0, (len(self.phrases) - 1))])
        self.lives = lives
        self.game_not_over = game_not_over
        self.factor = lives
        self.attempts = []

    def star_game(self):
        self.intro()
        while self.game_not_over:
            self.if_letter_guess(self.save_attempt(self.check_input()))
            print("attempt(s): " + ", ".join(self.attempts) + "\n")
            self.iterate_attempts()
            self.phrase.show()
            self.end(self.phrase.correct_phrase())
            self.incorrect_letter(self.iterate_attempts_incorrect())

    def intro(self):
        print(("*" * 65))
        print(("-" * 15) + " Welcome to the Pharse Hunter Game " + ("-" * 15))
        print(("-" * 22) + " made by Tomas Salas " + ("-" * 22))
        print(("*" * 65) + "\n")
        print("A little advice, start guessing with vowels Ex.(a,u). The first letter is always capitalized you have been warned 😬" + "\n")
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
                check = bool(re.search(r'[^A-Za-z]', letter))
                if check == False:
                    return letter
                else:
                    print("Oh no! that is not a valid character. Please try again")
                    continue
            else:
                print("Oh no! that is more than a letter. Please try again")
                continue

    def if_letter_guess(self, letter):
        if self.attempts.count(letter) >= 2:
            print("Oh no! You already try that letter 🕵. Please try again")
            self.if_letter_guess(self.save_attempt(self.check_input()))
        else:
            return

    def save_attempt(self, letter):
        self.attempts.append(letter)
        return letter

    def iterate_attempts(self):
        for attempt in self.attempts:
            self.phrase.iterate(attempt)

    def iterate_attempts_incorrect(self):
        save_result = self.phrase.incorrect_character(self.attempts[-1])
        return save_result

    def incorrect_letter(self, stringg):
        if stringg == True:
            print("You got that letter right! 💁")
        else:
            self.factor -= 1
            print("Oh no! You got {} lives out of {}".format(
                self.factor, self.lives) + " 🙈")
            if self.factor == 0:
                print(
                    "You run out of lives! Better luck next time 😉. If you are curious, below is the phrase you were trying to guess")
                self.phrase.all_correct()
                self.phrase.show()

                self.end(True)

    def end(self, booll):
        while booll:
            print("Would you like to try again? Type either \'YES\' or \'NO\'")
            answer = input(">    ")
            if answer.upper() == "YES":
                self.clear_attempts()
                self.phrase.phrase_reset_status()
                self.phrase.phrase_reset()
                game = Game(self.raw_phrases)
                game.star_game()
                sys.exit()
            elif answer.upper() == "NO":
                self.goodbye()
                sys.exit()
            else:
                print("Oh no! That is not a valid input. Type either \'YES\' or \'NO\' ")

    def clear_attempts(self):
        self.attempts.clear()
