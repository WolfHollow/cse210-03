
from ast import keyword
import random
from words import Word
from letters import Letters
class Game():


    def create_parachute(self, incorrect):
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

    def create_man(self):
        print('  O')
        print('/ | \ ')
        print(' / \ ')



    def get_input(self, guesses):
        self.guess = input('Guess a letter from a-z: ')
        if len(self.guess) == 1:
            if self.guess.isalpha() == True:
                if self.guess not in guesses:
                    return self.guess
                else:
                    print('You have already guessed that')
                    return self.guess
            else:
                print('Your guess is not a letter')
                return self.guess    
        else:
            print('Your guess is too long')
            return self.guess
            

    def create_lines(self, key):
        output = []
        for i in range(len(key)):
                    print('_', end='')
                    output.append('_')
        print('')
        return output

    def get_lines(self, output, key, guesses):
        for i in range(len(key)):
            for j in range(len(guesses)):
                if key[i] == guesses[j]:
                    output.pop(i)
                    output.insert(i, key[i])
        for i in range(len(key)):
            print(output[i], end='')
        print('')
        return output

    def main(self):
        obj = Word()
        key_word = obj.key_word
        key = key_word
        incorrect = 0
        win = False
        guesses = []
        word = []
        for i in range(len(key_word)):
            word.append('_')
        number = 0
        while win == False:
            self.create_parachute(incorrect)
            self.create_man()
            if number < 1:
                output = self.create_lines(key)
            else:
                total = self.get_lines(output, key, guesses)
                if '_' not in total:
                    win = True
                    print('Congradulations!!! You have won!!!')
            if win == False:
                input = self.get_input(guesses)
                guesses.append(input)
                if guesses[number] not in key:
                    incorrect += 1
                    print('You have guessed incorrectly')

                if incorrect == 5:
                    win = True
                    print('You have lost the game')
                number += 1
            
