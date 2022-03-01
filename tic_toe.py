# board
from ast import For
from itertools import count


Board = {'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' '}

boardkey = []

for key in Board:
    boardkey.append(key)


def printboard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def Game():
    turn = 'X'
    count = 0

    for i in range(10):
        printboard(Board)
        print('this is your turn,' + turn + 'Move this place')

        move = input()

        if Board[move] == ' ':
            Board[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves.
        if count >= 5:
            if Board['7'] == Board['8'] == Board['9'] != ' ':  # across the top
                printboard(Board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif Board['4'] == Board['5'] == Board['6'] != ' ':  # across the middle
                printboard(Board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif Board['1'] == Board['2'] == Board['3'] != ' ':  # across the bottom
                printboard(Board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif Board['1'] == Board['4'] == Board['7'] != ' ':  # down the left side
                printboard(Board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif Board['2'] == Board['5'] == Board['8'] != ' ':  # down the middle
                printboard(Board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif Board['3'] == Board['6'] == Board['9'] != ' ':  # down the right side
                printboard(Board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif Board['7'] == Board['5'] == Board['3'] != ' ':  # diagonal
                printboard(Board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif Board['1'] == Board['5'] == Board['9'] != ' ':  # diagonal
                printboard(Board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in boardkey:
            Board[key] = " "

        Game()


if __name__ == "__main__":
    Game()
