# gracz wybiera swój znak - done
# losujemy kto zaczyna (x czy o i odpowiednio pytanie o pole) - done
# komputer losuje pole - done
# pytamy gracza o pole - done
# jeśli pole zajęte, to info, że tutaj nie można postawić

# j.w. - komputer musi postawić na kolejny mwolnym
# sprawdzamy czy 3 pola obok siebie zajęte
# jeśli trzy zajęte obok siebie lub wszystkie zajęte, to koniec gry
# pytanie czy chce grać jeszcze raz - jak nie, kończymy


import random

print('*' * 38)
print("Hello! Welcome to the tic-tac-toe game!")
print('*' * 38)
print('\n')

name = input("Please, state your name: \n")
# game_board = [''] * 9
game_board = ['', 'X', 'X','X','X', 'X', 'X', 'X', '']


def choose_sign():
    print("Please choose if you want to be \'X\' or \'O\':\n")
    while True:
        player_choice = input()
        if player_choice.casefold() not in ['x', 'o']:
            print("Sorry, this is not a valid choice. Please choose \'X\' or \'O\':\n")
        else:
            if player_choice.casefold() == 'x':
                print(f"You have chosen \'X\'. I will be \'O\'")
                print("Let\'s start!")
                return player_choice
            else:
                print(f"You have chosen \'O\'. I will be \'X\'")
                print("Let\'s start!")
                return player_choice


def choose_order(player_sign, player_name):
    order = random.choice(['X', 'O'])
    if order == player_sign:
        print(f"{player_name}, you will go fist")
        return order
    else:
        print("Computer will play first")
        return order


def draw_board(board):  # tutaj funkcja game

    print('||'.center(17) + '||'.center(3))
    print(f" {board[0]}".center(8) + '||' + f"{board[1]}".center(9) + '||' + f" {board[2]}".center(8))
    print('||'.center(17) + '||'.center(3))
    print('---------' * 3)
    print('||'.center(17) + '||'.center(3))
    print(f" {board[3]}".center(8) + '||' + f"{board[4]}".center(9) + '||' + f" {board[5]}".center(8))
    print('||'.center(17) + '||'.center(3))
    print('---------' * 3)
    print('||'.center(17) + '||'.center(3))
    print(f" {board[6]}".center(8) + '||' + f"{board[7]}".center(9) + '||' + f" {board[8]}".center(8))
    print('||'.center(17) + '||'.center(3))


def comp_play(comp_sign):  #to nie działa!!

    game_on = True
    while game_on:
        computer_choice = random.randint(0, 8)
        if game_board[computer_choice]:
            pass # co tutaj ma być?
        else:
            game_board[computer_choice] += comp_sign
            game_on = False


def game(player_sign):
    game_on = True
    while game_on:
        print("Choose a field number from 1 to 9")
        player_choice = input()
        if not player_choice.isdigit() or 9 < int(player_choice) < 1:
            print("Sorry, this is not a valid choice. Choose a digit from 1 to 9")
        else:
            if game_board[int(player_choice) - 1]:
                print("Sorry, this field is already taken. Please choose another field number between 1 and 9.\n")
            else:
                game_board[int(player_choice) - 1] += player_sign
                game_on = False


def check_result():
    pass


comp_play('O')
draw_board(game_board)