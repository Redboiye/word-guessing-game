import random
from time import sleep
from word_functions import display_guessed_character
from choose_difficulty import get_difficulty

# 1d ir visa liste
# coordinates = [[1,2,3,4,5[1,2,3,4,5]], [1,2,3,4,5]] # 2d liste
# ieksa liste ir 3D dimensija

# 2D [
# [1,2,3,4,5]
# [1,2,3,4,5]
# [1,2,3,4,5]
# [1,2,3,4,5]
# [1,2,3,4,5]
# ]
# print(coordinates_2d[1][1])

# 3D
# coordinates_3d = [
# [1, 2, 3, 4, 5, [1, 2, 3, 4, 5]], [1, 2, 3, 4, 5]
# ]


words = [
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
easy_words = []
normal_words = []
hard_words = []
selected_difficulty = None
game_is_running = True
match_is_running = False
print("Welcome to the word guessing game!")
while game_is_running:

    print("Time to choose your difficulty!: ")
    while selected_difficulty is None:
        start_choice = input("e(easy), n(normal, h(hard) or q(quit): ")

        selected_difficulty, match_is_running = get_difficulty(
            words,
            easy_words,
            normal_words,
            hard_words,
            start_choice
        )

    print("Time to guess the word, Good luck!")
    random_word = random.choice(selected_difficulty)
    attempts = 10
    random_word_length = len(random_word)
    word_hidden_characters = []
    for character in range(random_word_length):
        word_hidden_characters.append('_')
    while match_is_running == True:
        print("you have left", attempts, "attempts")

        print(word_hidden_characters)
        player_guess = input("Make a guess: ")

        print("your guess : ", player_guess)
        if player_guess in random_word:
            word_hidden_characters = display_guessed_character(
                word_hidden_characters,
                random_word,
                player_guess,
            )
            print(word_hidden_characters)
        else:
            attempts = attempts - 1
        if attempts == 0:
            match_is_running = False
            selected_difficulty = None

            print("Sorry no more attempts")
            print("The word was", random_word)
            sleep(2)
        if random_word == word_hidden_characters:
            print("You won")
            match_is_running = False
            selected_difficulty = None
            # sleep(2)


