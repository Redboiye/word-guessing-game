import random
import csv
import os


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


class Match:
    attempts = 10

    def __init__(
            self,
            selected_difficulty,
            match_number
    ):
        self.result = None
        self.word_hidden_characters = []
        self.random_word = random.choice(selected_difficulty)
        self.random_word_length = len(self.random_word)
        self.match_number = match_number
        for character in range(self.random_word_length):
            self.word_hidden_characters.append('_')

    @staticmethod
    def __display_guessed_character(word_hidden_characters, random_word, player_guess) -> list:
        """accepts player guessed character, random word that he is guessing, and inserts the character inside
         it's place in the random word. The function returns the word with guessed and hidden characters."""
        player_guess_index = random_word.index(player_guess)
        word_hidden_characters[player_guess_index] = player_guess

        return word_hidden_characters

    def save_result(
            self,
            result,

    ):

        with open("record.csv", "a", newline='') as f:
            writer = csv.writer(f)
            word = "".join(self.random_word)
            records = [self.match_number, word, result]
            writer.writerow(records)

    @staticmethod
    def display_statistics():
        with open("record.csv", mode='r') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)

    def start(self, match_is_running):
        print("Time to guess the word, Good luck!")
        while match_is_running == True:
            print("you have left", self.attempts, "attempts")

            print(self.word_hidden_characters)
            player_guess = input("Make a guess: ")

            print("your guess : ", player_guess)
            if player_guess in self.random_word:
                self.word_hidden_characters = self.__display_guessed_character(
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
                self.save_result("False")
                print("Sorry no more attempts")
                print("The word was", self.random_word)
                return selected_difficulty, match_is_running
            if self.random_word == self.word_hidden_characters:
                print("You won")
                self.save_result("True")
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
    match_number = 1

    def __init__(self):
        file_name = "record.csv"
        if not os.path.exists(file_name):
            with open("record.csv", "w", newline='\n') as f:
                writer = csv.writer(f)
                headers = ["match_number", "word", "win"]
                writer.writerow(headers)

    @staticmethod
    def __get_difficulty(words, easy_words, normal_words, hard_words, start_choice):
        """Player can start choosing the difficult from easy to hard even quit. and function
        returns the selected difficulty for the word list that is already made, match_is_running is a boolion that
        makes sure that the player chosen difficulty is True"""

        selected_difficulty = None
        match_is_running = None
        hell_mode_word = [["p", "n", "e", "u", "m", "o", "n", "o", "u", "l", "t", "r",
                           "a", "m", "i", "c", "r", "o", "s", "c", "o", "p", "i",
                           "c", "s", "i", "l", "i", "c", "o", "v", "o", "l", "c", "a",
                           "n", "o", "c", "o", "n", "i", "o", "s", "i", "s"]]
        if start_choice == "q":
            exit("bye bye")
        if start_choice == "e":
            for word in words:
                if len(word) == 3:
                    easy_words.append(word)
            selected_difficulty = easy_words
            match_is_running = True

        if start_choice == "n":
            for word in words:
                if 3 < len(word) <= 7:
                    normal_words.append(word)
            selected_difficulty = normal_words
            match_is_running = True
        if start_choice == "h":
            for word in words:
                if len(word) >= 8:
                    hard_words.append(word)
            selected_difficulty = hard_words
            match_is_running = True

        if start_choice == "666":
            print("Welcome to HELL MODE!")
            selected_difficulty = hell_mode_word
            match_is_running = True

        return selected_difficulty, match_is_running,

    def start(self):
        print("Welcome to the word guessing game!")

        while self.game_is_running:
            print("Time to choose your difficulty!: ")
            while self.selected_difficulty is None:
                start_choice = input("e(easy), n(normal, h(hard), q(quit), r(records): ")

                if start_choice == 'r':
                    Match.display_statistics()
                    continue

                self.selected_difficulty, self.match_is_running = self.__get_difficulty(
                    WordSet.WORDS,
                    self.easy_words,
                    self.normal_words,
                    self.hard_words,
                    start_choice
                )

            match = Match(self.selected_difficulty, self.match_number)
            self.selected_difficulty, self.match_is_running = match.start(self.match_is_running)
            self.match_number += 1
