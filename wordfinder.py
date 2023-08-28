"""Word Finder: finds random words from a dictionary."""
from random import randint

class WordFinder:

    """
    Finds and returns a random word based on a text file path you input into the class

    >>> len(self.words) != 0

    """

    def __init__(self, words_file):
        self.words_file = words_file
        self.words = []

        with open (self.words_file, 'r') as file:
            lines = file.readlines()
            words = [line.strip() for line in lines]
            print(f'{len(words)} words read')
            self.words = words

    def random(self):
        length = len(self.words)
        rand_num = randint(0, length - 1)
        return self.words[rand_num]


class SpecialWordFinder(WordFinder):

    """
    Finds and returns a random word based on a text file path you input into the class that isn't blank or a comment

    >>>

    """

    def __init__(self, words_file):
        super().__init__(words_file)
        self.words = []

        with open (self.words_file, 'r') as file:
            lines = file.readlines()
            words = [line.strip() for line in lines if line.strip() and not line.startswith('#')]
            print(f'{len(words)} words read')
            self.words = words