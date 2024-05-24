import random
def add_new_number(board):
    #Add a new number to the board at a random empty location
    #80% chance of getting a 2, 20% chance of getting a 4
    empty = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                empty.append((i, j))
    if empty:
        i, j = random.choice(empty)
        board[i][j] = 2 if random.random() < 0.8 else 4
    return board
def print_board(board):
    #Print the board
    for row in board:
        print(' '.join([str(elem) for elem in row]))
    print()

def game_2048(rows):
    #Create a 2D list of size rows x rows with all elements as 0
    board = [[0 for i in range(rows)] for j in range(rows)]

    #Add 2 random numbers to the board
    board = add_new_number(board)
    board = add_new_number(board)

    #Print the board
    print("Welcome to 2048!")
    print("Use the following keys to move the tiles:")
    print("W: Move Up")
    print("S: Move Down")
    print("A: Move Left")
    print("D: Move Right")
    print("Q: Quit the game")
    print_board(board)

    #Loop until the game is over
    while True:
        #Get the user's move
        move = input("Enter your move: ").upper()

        #Move Up
        if move == 'W':
            for j in range(rows):
                i = 0
                while i < rows - 1:
                    for k in range(i + 1, rows):
                        if board[k][j] != 0:
                            if board[i][j] == 0:
                                board[i][j] = board[k][j]
                                board[k][j] = 0
                            elif board[i][j] == board[k][j]:
                                board[i][j] *= 2
                                board[k][j] = 0
                            break
                    i += 1

        #Move Down
        elif move == 'S':
            for j in range(rows):
                i = rows - 1
                while i > 0:
                    for k in range(i - 1, -1, -1):
                        if board[k][j] != 0:
                            if board[i][j] == 0:
                                board[i][j] = board[k][j]
                                board[k][j] = 0
                            elif board[i][j] == board[k][j]:
                                board[i][j] *= 2
                                board[k][j] = 0
                            break
                    i -= 1

        #Move Left
        elif move == 'A':
            for i in range(rows):
                j = 0
                while j < rows - 1:
                    for k in range(j + 1, rows):
                        if board[i][k] != 0:
                            if board[i][j] == 0:
                                board[i][j] = board[i][k]
                                board[i][k] = 0
                            elif board[i][j] == board[i][k]:
                                board[i][j] *= 2
                                board[i][k] = 0
                            break
                    j += 1

        #Move Right
        elif move == 'D':
            for i in range(rows):
                j = rows - 1
                while j > 0:
                    for k in range(j - 1, -1, -1):
                        if board[i][k] != 0:
                            if board[i][j] == 0:
                                board[i][j] = board[i][k]
                                board[i][k] = 0
                            elif board[i][j] == board[i][k]:
                                board[i][j] *= 2
                                board[i][k] = 0
                            break
                    j -= 1
                    
        #Quit the game
        elif move == 'Q':
            break

        #Add a new number to the board
        board = add_new_number(board)
        
        #Print the board
        print_board(board)

        #Check if the game is over
        game_over = True
        for i in range(rows):
            for j in range(rows):
                if board[i][j] == 0:
                    game_over = False
                    break
                if i > 0 and board[i][j] == board[i - 1][j]:
                    game_over = False
                    break
                if j > 0 and board[i][j] == board[i][j - 1]:
                    game_over = False
                    break

        if game_over:
            print("Game Over!")
            break


if __name__ == '__main__':
    print("Enter the number of rows and columns of the game 4 - 12:")
    rows = int(input("Rows: "))
    if rows <= 3:
        print("Invalid number of rows. Minium 4 rows required.")
        game_2048(4)
    elif rows > 12:
        print("Invalid number of rows. Maximum 12 rows allowed.")
        game_2048(12)
    else:
        game_2048(rows)