#Tic Tac Toe Game, Using functions, while loops, and if statments
# Author - Ethan Shaw
from words import get_word


def create_parachute(incorrect):
    if incorrect == 0:
        print(f' ㅡ')
        if incorrect < 2:
            print(f'/  \ ')
            if incorrect < 3:
                print('ㅡ ㅡ')
                if incorrect < 4:
                    print(f'\   /')
                    if incorrect < 5:
                        print(' \ /')

def create_man():
    print('  O')
    print('/ | \ ')
    print(' / \ ')      


def create_list():
    return [hi]
    
def get_input(guesses):
    guess = input('Guess a letter from a-z: ')
    if len(guess) == 1:
        if guess.isalpha() == True:
            if guess not in guesses:
                return guess
            else:
                print('You have already guessed that')
        else:
            print('Your guess is not a letter')
    else:
        print('Your guess is too long')
        
def main():
    incorrect = 0
    word_list = create_list()
    i = random.randint(0, len(word_list)-1)
    key_word = word_list[i]
    win = False
    guesses = []
    while win == False:
        get_input(guesses)
        create_parachute(incorrect)
        create_man()
        win = True
        
main()
