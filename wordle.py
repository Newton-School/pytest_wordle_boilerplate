import words


class GameLogic:
    def __init__(self, solution_word, number_of_guesses=6):
        self.solution_word = solution_word
        self.number_of_guesses = number_of_guesses
        self.guess_list = []
        self.current_guess_list = []
        self.current_guess = ''
        self.is_game_over = False
        self.is_game_won = False
        self.is_game_lost = False

    def add_next_letter_to_current_guess_list(self, letter):
        current_context = [letter, 0, 0]
        if letter in self.solution_word:
            current_context[1] = 1
            if letter == self.solution_word[len(self.current_guess_list)]:
                current_context[2] = 1
        self.current_guess_list.append(current_context)
        if len(self.get_current_guess_list()) == 5:
            is_current_guess_correct = self.check_the_current_guess()
            guess_list_length = len(self.guess_list)
            self.add_current_guess_to_guess_list()
            guess_list_length_after_adding = len(self.guess_list)
            if guess_list_length_after_adding > guess_list_length:
                if is_current_guess_correct:
                    self.is_game_won = True
                    self.is_game_over = True
                else:
                    self.number_of_guesses -= 1
                    if self.number_of_guesses == 0:
                        self.is_game_lost = True
                        self.is_game_over = True
            self.current_guess_list = []
        return self.current_guess_list

    def add_current_guess_to_guess_list(self):
        if self.check_current_guess_is_valid():
            self.guess_list.append(self.current_guess_list)
        return self.guess_list

    def check_current_guess_is_valid(self):
        # return True if current guess is valid else return False
        # current guess is valid if it is a valid word and it is 5 letter word
        return True

    # current_guess is list of List where the first letter denotes the user entered letter
    # and second letter denotes weather that letter is present in solution word or not.
    # and the third letter denotes weather the letter is present in the solution word in the correct position or not.
    def check_the_current_guess(self):
        current_guess_string = ''
        # write code here to test current guess
        # if current guess is correct return True else return False
        pass

    def get_guess_list(self):
        return self.guess_list

    def get_current_guess_list(self):
        return self.current_guess_list
