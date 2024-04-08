import random
import os 

logo = '''
888   d8b        888                   888                    
888   Y8P        888                   888                    
888              888                   888                    
888888888 .d8888b888888 8888b.  .d8888b888888 .d88b.  .d88b.  
888   888d88P"   888       "88bd88P"   888   d88""88bd8P  Y8b 
888   888888     888   .d888888888     888   888  88888888888 
Y88b. 888Y88b.   Y88b. 888  888Y88b.   Y88b. Y88..88PY8b.     
 "Y888888 "Y8888P "Y888"Y888888 "Y8888P "Y888 "Y88P"  "Y8888  '''


def board():
    board = f'\n  {pos[0]} | {pos[1]} | {pos[2]} \n'\
        f'  ----------\n'\
        f'  {pos[3]} | {pos[4]} | {pos[5]} \n'\
        f'  ----------\n'\
        f'  {pos[6]} | {pos[7]} | {pos[8]} \n'
    print(board)

def player_choice(n):
    player_choice = int(input(f'Please Player {n} choose a number: '))
    while type(pos[player_choice-1]) == str:
        player_choice = int(input(f'Please Player {n} choose an avalable number: '))
    return player_choice-1

def bot_number(pos):
    list_number = []
    for i in pos:
        if type(i) == int:
            list_number.append(i)
    bot_number = int(random.choice(list_number))
    return bot_number

def check_winner(pos):
    if pos[0] == pos[1] == pos[2] or pos[3] == pos[4] == pos[5] or pos[6] == pos[7] == pos[8] or \
        pos[0] == pos[3] == pos[6] or pos[1] == pos[4] == pos[7] or pos[2] == pos[5] == pos[8] or \
        pos[0] == pos[4] == pos[8] or pos[2] == pos[4] == pos[6] :
        return False
    else: 
        return True

def draw(pos):
    for i in pos:
        if type(i) == int:
            return False
    return True


game_over = False
while game_over==False:
    pos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    os.system('cls')
    print(logo)
    mode_game = input('\nWelcome to Tic Tac Toe\nDo you want to play vs a bot or a friend ? Type (B/F)  ').upper()
    
    if mode_game == 'B':
        board()
        print('Player 1 symbol = X\nBot symbol = O')

        continue_game = True
        while continue_game:
            player_1 = 1
            pos[player_choice(n=player_1)] = 'X'
            board()
            winner = 'player'
            continue_game = check_winner(pos)
            if not continue_game:
                break
            if draw(pos):
                winner = 'draw'
                break
            print(f'Bot choice is ...')
            pos[bot_number(pos)-1] = 'O'
            board()
            winner = 'bot'
            continue_game = check_winner(pos)

        if winner == 'player':
            print('Congratulations you win 👏')
        elif winner == 'bot': 
            print('Opps, Bot won the game. 😔')
        else :
            print('Ohh It is a draw!! Let\' try again ')

    else:
        board()
        print('Player 1 symbol = X\nPlayer 2 symbol = O')
        continue_game = True
        while continue_game:

            player_1 = 1 
            pos[player_choice(n=player_1)] = 'X'
            board()
            winner = 'player1'
            continue_game = check_winner(pos)
            if not continue_game:
                break
            if draw(pos):
                winner = 'draw'
                break
            player2 = 2
            pos[player_choice(n=player2)] = 'O'
            board()
            winner = 'player2'
            continue_game = check_winner(pos)

        if winner == 'player1':
            print('Congratulations Player 1 win the game 👏')
        elif winner == 'player2': 
            print('Congratulations Player 2 win the game 👏')
        else :
            print('Ohh It is a draw!! Let\' try again ')
    again = input('Do you want to play again ? (y/n): ').upper()
    if again == 'Y':
        continue
    else: 
        game_over = True


