from wordle import GameLogic


def test_game_won():
    game_logic = GameLogic('hello')
    game_logic.add_next_letter_to_current_guess_list('h')
    game_logic.add_next_letter_to_current_guess_list('e')
    game_logic.add_next_letter_to_current_guess_list('l')
    game_logic.add_next_letter_to_current_guess_list('l')
    game_logic.add_next_letter_to_current_guess_list('o')
    assert game_logic.is_game_won
    assert game_logic.is_game_over


def test_dec_guesses():
    game_logic = GameLogic('hello')
    game_logic.add_next_letter_to_current_guess_list('h')
    game_logic.add_next_letter_to_current_guess_list('e')
    game_logic.add_next_letter_to_current_guess_list('l')
    game_logic.add_next_letter_to_current_guess_list('l')
    game_logic.add_next_letter_to_current_guess_list('p')
    assert game_logic.number_of_guesses == 5
    assert not game_logic.is_game_over
    assert not game_logic.is_game_lost


def test_game_over():
    game_logic = GameLogic('hello')
    for _ in range(6):
        game_logic.add_next_letter_to_current_guess_list('h')
        game_logic.add_next_letter_to_current_guess_list('e')
        game_logic.add_next_letter_to_current_guess_list('l')
        game_logic.add_next_letter_to_current_guess_list('l')
        game_logic.add_next_letter_to_current_guess_list('p')
    assert game_logic.number_of_guesses == 0
    assert game_logic.is_game_over
    assert game_logic.is_game_lost


def test_can_add_single_letter():
    game_logic = GameLogic('hello')
    game_logic.add_next_letter_to_current_guess_list('h')
    assert game_logic.current_guess_list == [['h', 1, 1]]


def check_can_handle_wrong_letter():
    game_logic = GameLogic('hello')
    game_logic.add_next_letter_to_current_guess_list('p')
    assert game_logic.current_guess_list == [['p', 0, 0]]


def test_can_handle_wrong_guess():
    game_logic = GameLogic('hello')
    game_logic.add_next_letter_to_current_guess_list('s')
    game_logic.add_next_letter_to_current_guess_list('h')
    game_logic.add_next_letter_to_current_guess_list('e')
    game_logic.add_next_letter_to_current_guess_list('l')
    game_logic.add_next_letter_to_current_guess_list('l')

    assert game_logic.guess_list == [[['s', 0, 0], ['h', 1, 0], ['e', 1, 0], ['l', 1, 1], ['l', 1, 0]]]
    assert game_logic.current_guess_list == []
    assert game_logic.number_of_guesses == 5


def test_wrong_word_not_present_in_dictionary():
    game_logic = GameLogic('hello')
    game_logic.add_next_letter_to_current_guess_list('s')
    game_logic.add_next_letter_to_current_guess_list('h')
    game_logic.add_next_letter_to_current_guess_list('e')
    game_logic.add_next_letter_to_current_guess_list('l')
    game_logic.add_next_letter_to_current_guess_list('p')
    assert game_logic.guess_list == []
    assert game_logic.current_guess_list == []
    assert game_logic.number_of_guesses == 6


