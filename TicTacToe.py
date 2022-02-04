#Tic Tac Toe Game, Using functions, while loops, and if statments
# Author - Ethan Shaw
from words import get_word


def create_parachute(incorrect):
    if incorrect == 0:
        print(f'ㅡㅡ')
        if incorrect < 2:
            print(f'/  ∖')
            if incorrect < 3:
                print('ㅡㅡ')
                if incorrect < 4:
                    print(f'∖  /')
                    if incorrect < 5:
                        print('∖  /')
def create_parachute(incorrect):
    if incorrect == 0:
        print(f'ㅡㅡ')
        if incorrect < 2:
            print(f'/  ∖')
            if incorrect < 3:
                print('ㅡㅡ')
                if incorrect < 4:
                    print(f'∖  /')
                    if incorrect < 5:
                        print('∖  /')
def create_man():
    print('O')
    print('/ | ∖')
    print('/ ∖')
                        


def create_list():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]


    
def get_input(guesses):
    guess = input('Guess a letter from a-z')
    if len(guess) == 1:
        if guess.isalpha() == True:
            if guess not in guesses:
                return guess
def main():
    incorrect = 0
    word = get_word()
    win = False
    while win == False:
        create_parachute(incorrect)
        create_man()
        
main()
