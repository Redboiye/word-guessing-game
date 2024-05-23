
def display_guessed_character(word_hidden_characters, random_word, player_guess) -> list:
    """accepts player guessed character, random word that he is guessing, and inserts the character inside
     it's place in the random word. The function returns the word with guessed and hidden characters."""
    player_guess_index = random_word.index(player_guess)
    word_hidden_characters[player_guess_index] = player_guess

    return word_hidden_characters
