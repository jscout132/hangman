from words import word 
from random import randint
num = randint(1,16)

print(num)
# look up where to pull the randint module from again
# might need some regex to ensure the player doesn't guess a number or special character

# s_word is the secret word
# h_word is the hidden word
# TODO update hidden_word to be just h_word

class Game():
    s_word = 'pancake'
    response = True
    word_check = ''

    def __init__(self, p_guess, order, hidden_word):
        self.p_guess = p_guess
        self.order = order
        self.hidden_word = hidden_word

    # TODO create function to pull a random word from a list of words

    # prepping the word to viewed by the player
    def modWord(self):
        self.order = list(enumerate(self.s_word))
        self.hidden_word = list('_' * len(self.s_word))
        return self.order, self.hidden_word

    # checking the format of the guess
    def checkGuess(self):
        self.p_guess = input('Guess a letter: ')
        # TODO need to set this up as a while loop
        if len(self.p_guess) >= 2:
            print('you can only guess one letter at a time')
        return self.p_guess

    def guessLetter(self):
        self.word_check = self.hidden_word
        for i in range(len(self.order)):
            if self.p_guess in self.order[i]:
                self.hidden_word[self.order[i][0]] = self.order[i][1]

        return self.hidden_word, self.word_check
    
    def comparison(self):
        if self.word_check == self.hidden_word:
            self.response = False
        print(self.s_word, self.hidden_word)



play = Game('','','')

def hangman():
    print('let\'s play hangman')
    Game.modWord(play)
    print(f'The word is {len(play.s_word)} letters long: ',' '.join(play.hidden_word))
    Game.checkGuess(play)
    counter = 3
    while counter > 0:
        Game.guessLetter(play)
        print(play.response)
        print(''.join(play.hidden_word), play.s_word)
        Game.comparison(play)
        if play.response == True:
            print(f'{play.p_guess} is in the word!')
            print(f'{play.hidden_word}')
        else:
            print('in the else')
            counter -= 1
        print('end of while', counter)
        Game.checkGuess(play)

        
        


hangman()