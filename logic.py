import random

SPACER = "------------------"

def winCondition(board):
    winner = 0 #0 - nikt, 1-gracz 1, 2-gracz 2

    #poziomo
    if board[0] == board[1] and board[1] == board[2] and board[2] != "[ ]":
        if board[0] == "[X]":
            winner = 1
        if board[0] == "[O]":
            winner = 2
    elif board[3] == board[4] and board[4] == board[5] and board[5] != "[ ]":
        if board[3] == "[X]":
            winner = 1
        if board[3] == "[O]":
            winner = 2
    elif board[6] == board[7] and board[7] == board[8] and board[8] != "[ ]":
        if board[6] == "[X]":
            winner = 1
        if board[6] == "[O]":
            winner = 2
    #pionowo
    elif board[0] == board[3] and board[3] == board[6] and board[6] != "[ ]":
        if board[0] == "[X]":
            winner = 1
        if board[0] == "[O]":
            winner = 2
    elif board[1] == board[4] and board[4] == board[7] and board[7] != "[ ]":
        if board[1] == "[X]":
            winner = 1
        if board[1] == "[O]":
            winner = 2
    elif board[2] == board[5] and board[5] == board[8] and board[8] != "[ ]":
        if board[2] == "[X]":
            winner = 1
        if board[2] == "[O]":
            winner = 2
    #przekatne
    elif board[0] == board[4] and board[4] == board[8] and board[8] != "[ ]":
        if board[0] == "[X]":
            winner = 1
        if board[0] == "[O]":
            winner = 2
    elif board[2] == board[4] and board[4] == board[6] and board[6] != "[ ]":
        if board[2] == "[X]":
            winner = 1
        else:
            winner = 2
    return winner


def startMenu():
    while 1:
        print("Kolko i krzyzyk!")
        print("1.Gra dla 2 graczy")
        print("2.Gra z komputerem")
        userChoice = input(">")
        if userChoice in ["1","2"]:
            return int(userChoice)
        else:
            print(SPACER)


def drawBoard(board):
    print(board[0],board[1],board[2])
    print(board[3],board[4],board[5])
    print(board[6],board[7],board[8])


def possibleMoves(board):
    moves = []
    i = 0
    for move in board:
        if move == "[ ]":
            moves.append(i)
        i += 1
    return moves


def playerMove(board, who):
    char = ""
    if who == 1:
        char = "X"
    elif who == 2:
        char = "O"
    while 1:
        print(f"Ruch gracza {who}, {char}:")
        move = input("Nr pola (1-9): ")
        try:
            move = int(move)
            move -= 1
            if move >= 0 and move <= 8:
                if board[move] == "[ ]":
                    board[move] = f"[{char}]"
                    break
                else:
                    print("Ruch niedozwolony!")
            else:
                print("Ruch niedozwolony!")
        except:
            print("Ruch niedozwolony!")
    return board


def computerMove(board, freeSpaces):
    # who = 2
    char = "O" 
    boardCopy = board[:]

    #czy nastepny ruch komputera jest wygrywajacy
    for move in freeSpaces: #np [1, 2]
        boardCopy[move] = "[O]"
        if winCondition(boardCopy) == 2:
            board[move] = f"[{char}]"
            print(f"Ruch komputera: {move+1}")
            # print("debug:komputer wygrywa")
            return board
        else:
            boardCopy[move] = "[ ]"

    #czy nastepny ruch czlowieka jest wygrywajacy
    for move in freeSpaces: #np [1, 2]
        boardCopy[move] = "[X]"
        if winCondition(boardCopy) == 1:
            board[move] = f"[{char}]"
            print(f"Ruch komputera: {move+1}")
            # print("debug:czlowiek wygrywa")
            return board
        else:
            boardCopy[move] = "[ ]"
    
    #jesli zaczyna to wez korner
    if len(freeSpaces) == 9:
        move = random.choice([0,2,6,8])
        board[move] = f"[{char}]"
        print(f"Ruch komputera: {move+1}")
        # print("debug:zaczynam_losowy_korner")
        return board

    #jezeli srodek jest wolny to go wez
    if 4 in freeSpaces:
        board[4] = f"[{char}]"
        # print("debug:srodek")
        print(f"Ruch komputera: {5}")
        return board

    #jezeli wolna krawedz to ja wez
    edgesOpen = []
    for move in freeSpaces:
        if move in [1,3,5,7]:
            edgesOpen.append(move)
    if len(edgesOpen) > 0:
        move = random.choice(edgesOpen)
        board[move] = f"[{char}]"
        print(f"Ruch komputera: {move+1}")
        # print("debug:krawedz")
        return board

    #losowe ruchy do testow
    else:
        move = random.choice(freeSpaces)
        board[move] = f"[{char}]"
        print("debug:rand")
        print(f"Ruch komputera: {move+1}")
        return board