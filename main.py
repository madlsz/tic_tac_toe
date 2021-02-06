"""
    ##############
    #   |   |   #
    #---|---|---#
    #   | x | x #
    #---|---|---#
    #   |   |   #
    ##############

"""

#player 1 is X
#player 2 is O

#todo: dodac ai; umozliwic  zmiane kolejnosci graczy

import random
from logic import winCondition, startMenu, drawBoard, playerMove, computerMove, possibleMoves

SPACER = "------------------"

def main():
    board = ["[ ]","[ ]","[ ]",
             "[ ]","[ ]","[ ]",
             "[ ]","[ ]","[ ]"]

    gameType = startMenu()

    #gra dla 2 graczy
    if gameType == 1:
        i = 0
        while 1:
            if i > 8:
                break

            
            drawBoard(board)
            print(SPACER)
            board = playerMove(board,1)
            i += 1
            win = winCondition(board)
            if win != 0:
                break
            
            
            drawBoard(board)
            print(SPACER)
            board = playerMove(board,2)
            i += 1
            win = winCondition(board)
            if win != 0:
                break

    #gra z komputerem
    elif gameType == 2:
        i = 0

        #losowanie kolejnosci
        kolejnosc = random.choice([1,2])
        if kolejnosc == 1:
            pass
        else:
            print("zaczyna komputer")
            # drawBoard(board)
            # print(SPACER)
            freeSpaces = possibleMoves(board)
            board = computerMove(board, freeSpaces)
            i += 1

        while 1:
            if i > 8:
                break

            
            drawBoard(board)
            print(SPACER)
            board = playerMove(board,1)
            i += 1
            win = winCondition(board)
            if win != 0:
                break

            if i > 8:
                break

            
            drawBoard(board)
            print(SPACER)
            freeSpaces = possibleMoves(board)
            board = computerMove(board, freeSpaces)
            i += 1
            win = winCondition(board)
            if win != 0:
                break


    print(SPACER)
    drawBoard(board)
    if win != 0:
        print(f"Gracz {win} wygral!")
    else:
        print("Remis!")

    input()

if __name__ == "__main__":
    main()