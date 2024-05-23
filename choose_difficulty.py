def get_difficulty(words, easy_words, normal_words, hard_words, start_choice):
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

    #  def - A function is a block of code which only runs when it is called.
    # You can pass data, known as parameters, into a function.
    # The return keyword is to exit a function and return a value.
