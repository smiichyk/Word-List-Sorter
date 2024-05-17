# constants for messages and prompts displayed to the user
MAX_WORDS_LIMIT = 1000
WELCOME = 'Welcome to the Word/Phrase List Sorter!'
ENTER_CHOICE = 'Enter your choice (1 or 2): '
INVALID_CHOICE = '\nInvalid choice. Please enter a valid option\n'
ENTER_LIST_OR_PATH = '\nEnter a list of words or phrases, or specify the path to a .txt file containing your list: '
MORE_THAN_1_WORD = '\nThe list should have more than 1 word.'


class Calculate:
    """ Class to handle sorting of words or phrases. """
    def __init__(self, ascending: bool = False, ignore_case: bool = False, words_or_path: str = None):
        """
        initialize a Calculate object.

        parameters:
            ascending (bool): If True, sort words in ascending order. default is False.
            ignore_case (bool): If True, ignore case sensitivity when sorting. default is False.
            words (str): A comma-separated string of words or a path to a text file containing words.
        """
        self.ascending = ascending
        self.ignore_case = ignore_case
        self.words_or_path = words_or_path

    def calculate(self):
        """
        Perform sorting based on object attributes.

        Returns:
            str: A sorted comma-separated string of words.
        """
        words_list = []

        if self.words_or_path is not None:
            # Splitting input words by comma and stripping extra spaces
            for word in self.words_or_path.split(', '):
                words_list.append(word.strip())
        else:
            print('\nThe list is empty.')
            return None

        if len(words_list) == 1:
            try:
                # Attempting to open a file if only one entry is provided
                with open(words_list[0]) as path_txt:
                    words_list = []
                    words_list_txt = path_txt.read()
                    for word in words_list_txt.split(','):
                        words_list.append(word.strip())
            except FileNotFoundError:
                if '.txt' in words_list[0]:
                    print('\nFile not found.')
                    return None
                else:
                    print(MORE_THAN_1_WORD)
                    return None

        if 1 < len(words_list) <= MAX_WORDS_LIMIT:
            # Sorting based on conditions
            if self.ascending:
                if self.ignore_case:
                    words_list.sort(key=str.lower)
                if not self.ignore_case:
                    words_list.sort()
            elif not self.ascending:
                if self.ignore_case:
                    words_list.sort(key=str.lower, reverse=True)
                if not self.ignore_case:
                    words_list.sort(reverse=True)
            return str(', '.join(words_list))

        else:
            print('\nIn the list, there should be no more than 1000 words.')
            return None


def ignore_case_choice(calculate: Calculate):
    """
    Function to handle case sensitivity choice.

    Parameters:
        calculate (Calculate): An instance of Calculate class.
    """
    print('\n1. Ignore case\n2. Consider case\n')
    ignore_case = input(ENTER_CHOICE)

    if ignore_case == '1':
        calculate.ignore_case = True
        list_or_path = input(ENTER_LIST_OR_PATH)
        calculate.words_or_path = list_or_path
        if calculate.calculate() is not None:
            print(f'\nSorted list: {calculate.calculate()}')

    elif ignore_case == '2':
        calculate.ignore_case = False
        list_or_path = input(ENTER_LIST_OR_PATH)
        calculate.words_or_path = list_or_path
        if calculate.calculate() is not None:
            print(f'\nSorted list: {calculate.calculate()}')

    else:
        print(INVALID_CHOICE)


def main_menu():
    """ Main function to display menu options and handle user choices. """
    calculate = Calculate()
    print(WELCOME)
    while True:
        print('\nSelect an option:\n1. Sort a list of words or phrases\n2. Exit\n')
        continue_or_quit = input(ENTER_CHOICE)

        if continue_or_quit == '1':
            print('\n1. Ascending\n2. Descending\n')
            asccending_or_descending = input(ENTER_CHOICE)

            if asccending_or_descending == '1':
                calculate.ascending = True
                ignore_case_choice(calculate)

            elif asccending_or_descending == '2':
                calculate.ascending = False
                ignore_case_choice(calculate)

        elif continue_or_quit == '2':
            print('Quiting...')
            break

        else:
            print(INVALID_CHOICE)


if __name__ == '__main__':
    main_menu()
