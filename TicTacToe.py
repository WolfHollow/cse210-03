#Tic Tac Toe Game, Using functions, while loops, and if statments
# Author - Ethan Shaw
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
                        
def get_input_X(spaces):
    selected_space = int(input('Which space would you like to add an x to?'))
    while 5 != 0:
        if selected_space in spaces:
            return selected_space
        else:
            print('Please enter a valid space')
            selected_space = int(input('Which space would you like to add an x to?'))
    
def add_X(s, spaces):
    s = s - 1
    spaces[s] = 'x'
def get_input_O(spaces):
    selected_space = int(input('Which space would you like to add an o to?'))
    while 5 != 0:
        if selected_space in spaces:
            return selected_space
        else:
            print('Please enter a valid space')
            selected_space = int(input('Which space would you like to add an x to?'))
def add_O(s, spaces):
    s = s - 1
    spaces[s] = 'o'

def create_list():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]

def check_x_win(spaces):
    row_1 = spaces[0:3]
    row_2 = spaces[3:6]
    row_3 = spaces[6:9]
    if row_2[1] == 'x':
        if row_1[0] == 'x':
            if row_3[2] =='x':
                return True
        elif row_1[2] == 'x':
            if row_3[0] == 'x':
                return True
    if row_2 and row_3 and row_1 == ['x', 'x', 'x']:
        return True
    if row_1[0] == 'x' and row_2[0] == 'x' and row_3[0] == 'x':
        return True
    if row_1[1] == 'x' and row_2[1] == 'x' and row_3[1] == 'x':
        return True
    if row_1[2] == 'x' and row_2[2] == 'x' and row_3[2] == 'x':
        return True
    return False

def check_o_win(spaces):
    row_1 = spaces[0:3]
    row_2 = spaces[3:6]
    row_3 = spaces[6:9]

    if row_2[1] == 'o':
        if row_1[0] == 'o':
            if row_3[2] =='o':
                return True
        elif row_1[2] == 'o':
            if row_3[0] == 'o':
                return True
    if row_2 and row_3 and row_1 == ['o', 'o', 'o']:
        return True
    if row_1[0] == 'o' and row_2[0] == 'o' and row_3[0] == 'o':
        return True
    if row_1[1] == 'o' and row_2[1] == 'o' and row_3[1] == 'o':
        return True
    if row_1[2] == 'o' and row_2[2] == 'o' and row_3[2] == 'o':
        return True
    
def get_input(guesses):
    guess = input('Guess a letter from a-z')
    if len(guess) == 1:
        if guess.isalpha() == True:
            if guess not in guesses:
                return guess
def main():
    incorrect = 0
    word_list = create_list()
    i = random.randint(0, len(word_list))
    key_word = word_list[i]
    win = False
    while win == False:
        create_parachute(incorrect)
        create_man()
        
main()
