import random

def draw_board(board):
    # This function prints out the board that it was passed and should not return anything
    #HINT: the parameter board should hold a list that holds the position of 'X's and 'O's
    print('   |   |')
    print(' '  board[7]  ' | '  board[8]  ' | '  board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '  board[4]  ' | '  board[5]  ' | '  board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '  board[1]  ' | '  board[2]  ' | '  board[3])
    print('   |   |')
    print('\n')
    return

def input_player_letter():
    #Ask the player if they want to be 'X' or 'O'
    #Return the chosen letter
    #Hint: Use a loop to keep prompting the player for a letter if the input is not valid
    letter = ""
    while (letter != 'X' and letter != 'O'):
      letter = input("Choose to be player X or player O\n").upper()  
    return letter

def who_goes_first():
    #Randomly choose who goes first
    #Return the string 'computer' or 'player'
    #HINT: look up the documentation for the 'random' library

    return

def main():

    print ('Welcome to Tic Tac Toe')
    turn = who_goes_first()

    player_letter = input_player_letter()
    #Here assign computer_letter to be 'O' if player_letter is 'X' or vice versa



    # Initialize your board list here to pass to draw_board
    #board =
    draw_board(board)

main()
