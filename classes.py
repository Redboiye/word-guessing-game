from time import sleep

from choose_difficulty import get_difficulty
import random

from word_functions import display_guessed_character


class WordSet:
    WORDS = [
        ["c", "a", "r"],
        ["d", "i", "g"],
        ["b", "a", "t"],
        ["t", "o", "g"],
        ["c", "o", "d"],
        ["h", "a", "t"],
        ["m", "o", "g"],
        ["f", "o", "g"],
        ["b", "i", "g"],
        ["t", "i", "g", "e", "r"],
        ["d", "o", "l", "p", "h", "i", "n"],
        ["s", "q", "u", "i", "r", "r", "e", "l"],
        ["c", "h", "i", "m", "p", "a", "n", "z", "e"],
        ["l", "i", "z", "a", "r", "d"],
        ["r", "h", "i", "n", "o", "c", "e", "r", "o", "s"],
        ["h", "y", "e", "n", "a"],
        ["e", "l", "e", "p", "h", "a", "n", "t"],
        ["g", "i", "r", "a", "f", "f", "e"],
        ["h", "i", "p", "p", "o", "p", "o", "t", "a", "m", "u", "s"]
    ]


class Player:
    pass


class Match:
    attempts = 10

    def __init__(
            self,
            selected_difficulty,
    ):
        self.word_hidden_characters = []
        self.random_word = random.choice(selected_difficulty)
        self.random_word_length = len(self.random_word)
        for character in range(self.random_word_length):
            self.word_hidden_characters.append('_')

    def start(self, match_is_running):
        print("Time to guess the word, Good luck!")
        while match_is_running == True:
            print("you have left", self.attempts, "attempts")

            print(self.word_hidden_characters)
            player_guess = input("Make a guess: ")

            print("your guess : ", player_guess)
            if player_guess in self.random_word:
                self.word_hidden_characters = display_guessed_character(
                    self.word_hidden_characters,
                    self.random_word,
                    player_guess,
                )
                print(self.word_hidden_characters)
            else:
                self.attempts = self.attempts - 1
            if self.attempts == 0:
                match_is_running = False
                selected_difficulty = None

                print("Sorry no more attempts")
                print("The word was", self.random_word)
                sleep(2)
                return selected_difficulty, match_is_running
            if self.random_word == self.word_hidden_characters:
                print("You won")
                match_is_running = False
                selected_difficulty = None
                # sleep(2)

                return selected_difficulty, match_is_running


class Game:
    easy_words = []
    normal_words = []
    hard_words = []
    selected_difficulty = None
    game_is_running = True
    match_is_running = False

    def start(self):
        print("Welcome to the word guessing game!")

        while self.game_is_running:
            print("Time to choose your difficulty!: ")
            while self.selected_difficulty is None:
                start_choice = input("e(easy), n(normal, h(hard), q(quit): ")

                self.selected_difficulty, self.match_is_running = get_difficulty(
                    WordSet.WORDS,
                    self.easy_words,
                    self.normal_words,
                    self.hard_words,
                    start_choice
                )

            match = Match(self.selected_difficulty)
            self.selected_difficulty, self.match_is_running = match.start(self.match_is_running)
