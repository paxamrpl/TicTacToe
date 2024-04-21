player_1 = input("Игрок № 1 выбирите x или 0: ")
if player_1 == "x":
    player_2 = "0"
    player_1 = "x"
else:
    player_2 = "x"
    player_1 = "0"

print(f"Игрок № 1 выбрал {player_1}, а Игрок № 2 выбрал {player_2}")

board = [" " for x in range(9)]

def startGame():
   print("Добро пожаловать в крестики - нолики!")
   printBoard()
   playerTurn("1")
def printBoard():
   print("     |     |     ")
   print("  " + board[0] + "  |  " + board[1] + "  |  " + board[2] + "  ")
   print("_____|_____|_____")
   print("     |     |     ")
   print("  " + board[3] + "  |  " + board[4] + "  |  " + board[5] + "  ")
   print("_____|_____|_____")
   print("     |     |     ")
   print("  " + board[6] + "  |  " + board[7] + "  |  " + board[8] + "  ")
def playerTurn(turn):
   print(f"Игрок № {turn}, ваш ход!")
   position = input("Выбирите позицию от 1 до 9: ")
   while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
       position = input("Неверная позиция! Выбирите позицию от 1 до 9: ")

   position = int(position)

   symbol = player_1 if turn == "1" else player_2

   if board[position - 1] == " ":
        board[position - 1] = symbol
        printBoard()
        if checkWin():
            return

        turn = "2" if turn == "1" else "1"
        playerTurn(turn)
   else:
        print("Эта позиция уже занята!")
        playerTurn(turn)
def checkWin():
    for i in range(0, 3):
        if board[i] == board[i + 3] == board[i + 6] != " ":
            if board[i] == player_1:
                print("Игрок № 1 побкдил!")
            elif board[i] == player_2:
                print("Игрок № 2 победил!")
            return True
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != " ":
            if board[i] == player_1:
                print("Игрок № 1 побкдил!")
            elif board[i] == player_2:
                print("Игрок № 2 победил!")
            return True
    if board[0] == board[4] == board[8] != " ":
        if board[0] == player_1:
            print("Игрок № 1 побкдил!")
        elif board [0] == player_2:
            print("Игрок № 2 победил!")
        return True
    if board[2] == board[4] == board[6] != " ":
        if board[2] == player_1:
            print("Игрок № 1 побкдил!")
        elif board[2] == player_2:
            print("Игрок № 2 победил!")
        return True
    if " " not in board:
        print("Ничья! Побкдила дружба!")
        return True

startGame()

