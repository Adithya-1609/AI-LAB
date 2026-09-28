import random

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

print("TIC TAC TOE")
print("You = X")
print("Computer = O")

while True:

    # Display board
    print("\n", board[0], "|", board[1], "|", board[2])
    print("---+---+---")
    print("", board[3], "|", board[4], "|", board[5])
    print("---+---+---")
    print("", board[6], "|", board[7], "|", board[8])


    position = int(input("Enter position (1-9): ")) - 1

    if board[position] != " ":
        print("Position already taken!")
        continue

    board[position] = "X"


    if ((board[0] == board[1] == board[2] == "X") or
        (board[3] == board[4] == board[5] == "X") or
        (board[6] == board[7] == board[8] == "X") or
        (board[0] == board[3] == board[6] == "X") or
        (board[1] == board[4] == board[7] == "X") or
        (board[2] == board[5] == board[8] == "X") or
        (board[0] == board[4] == board[8] == "X") or
        (board[2] == board[4] == board[6] == "X")):

        print("You win!")
        break

    # Computer move
    empty = []

    for i in range(9):
        if board[i] == " ":
            empty.append(i)

    if len(empty) == 0:
        print("It's a draw!")
        break

    computer = random.choice(empty)
    board[computer] = "O"

    print("Computer selected position:", computer + 1)

    # Check computer win
    if ((board[0] == board[1] == board[2] == "O") or
        (board[3] == board[4] == board[5] == "O") or
        (board[6] == board[7] == board[8] == "O") or
        (board[0] == board[3] == board[6] == "O") or
        (board[1] == board[4] == board[7] == "O") or
        (board[2] == board[5] == board[8] == "O") or
        (board[0] == board[4] == board[8] == "O") or
        (board[2] == board[4] == board[6] == "O")):

        print("Computer wins!")
        break