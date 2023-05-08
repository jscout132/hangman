from words import word 
from random import randint
num = randint(1,16)

# might need some regex to ensure the player doesn't guess a number or special character

# s_word is the secret word
# TODO update h_word to be just h_word
# TODO to track the letters that have already been guessed

class Game():
    # TODO set up s_word to pull from the list of imported words using a randint
    s_word = 'pancake'
    response = True
    word_check = ''
    counter = 3

    def __init__(self, p_guess, order, h_word):
        self.p_guess = p_guess
        self.order = order
        self.h_word = h_word

    # TODO create function to pull a random word from a list of words

    # prepping the word to viewed by the player
    def modWord(self):
        self.order = list(enumerate(self.s_word))
        self.h_word = list('_' * len(self.s_word))
        return self.order, self.h_word

    # checking the format of the guess
    def checkGuess(self):
        self.p_guess = input('Guess a letter: ')
        # TODO need to set this up as a while loop 
        # TODO set up regex here booooo
        if len(self.p_guess) >= 2:
            print('you can only guess one letter at a time')
        return self.p_guess

    def guessLetter(self):
        self.word_check = self.h_word[:]
        print('word check', self.word_check, 'hidden word', self.h_word)
        for i in range(len(self.order)):
            if self.p_guess in self.order[i]:
                self.h_word[self.order[i][0]] = self.order[i][1]
        print('word check', self.word_check, 'hidden word', self.h_word)

        return self.h_word, self.word_check
    
    def comparison(self):
        if self.word_check == self.h_word:
            self.counter -= 1
            print(self.p_guess,'is not in the word')
        else:
            print(self.p_guess, 'is in the word')
        return self.response



play = Game('','','')

def hangman():
    print('let\'s play hangman')

    Game.modWord(play)
    print(f'The word is {len(play.s_word)} letters long: ',' '.join(play.h_word))
    Game.checkGuess(play)
    while play.counter > 0:
        Game.guessLetter(play)

        # handling the word comparisons
        Game.comparison(play)

        Game.checkGuess(play)


hangman()