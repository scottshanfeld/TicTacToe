# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class tictactoe:

    def __init__(self):
        self.board = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]

    def takeSpace(self, piece, row, col):
        if row == 'top':
            y = 0
        elif row == 'middle':
            y = 1
        elif row == 'bottom':
            y = 2

        if col == 'left':
            x = 0
        elif col == 'middle':
            x = 1
        elif col == 'right':
            x = 2

        if self.board[y][x] == " ":
            self.board[y][x] = piece
        else:
            print("This space was already taken.")

    def checkWin(self):
        won = False
        tie = True
        if self.board[0][0] != " " and self.board[0][0] == self.board[0][1] and self.board[0][1] == self.board[0][2]:
            winner = self.board[0][0]
            won = True
        elif self.board[1][0] != " " and self.board[1][0] == self.board[1][1] and self.board[1][1] == self.board[1][2]:
            winner = self.board[1][0]
            won = True
        elif self.board[2][0] != " " and self.board[2][0] == self.board[2][1] and self.board[2][1] == self.board[2][2]:
            winner = self.board[2][0]
            won = True
        elif self.board[0][0] != " " and self.board[0][0] == self.board[1][0] and self.board[1][0] == self.board[2][0]:
            winner = self.board[0][0]
            won = True
        elif self.board[0][1] != " " and self.board[0][1] == self.board[1][1] and self.board[1][1] == self.board[2][1]:
            winner = self.board[0][1]
            won = True
        elif self.board[0][2] != " " and self.board[0][2] == self.board[1][2] and self.board[1][2] == self.board[2][2]:
            winner = self.board[0][2]
            won = True
        elif self.board[0][0] != " " and self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            winner = self.board[0][0]
            won = True
        elif self.board[0][2] != " " and self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
            winner = self.board[0][2]
            won = True

        if not won:
            for eachRow in self.board:
                if eachRow.count(' ') > 0:
                    tie = False

        if won:
            print(winner + " Wins!")
            return True
        elif tie:
            print("It's a tie.")
            return True
        else:
            return False

    def showBoard(self):
        print(" " + self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2] + " ")
        print("---+---+---")
        print(" " + self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2] + " ")
        print("---+---+---")
        print(" " + self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2] + " ")

    def playGame(self):
        turn = 0
        while(not self.checkWin()): #also returns true if a tie
            self.showBoard()
            if turn % 2 == 0:
                print("O's Turn!")
                piece = "O"
                move = input("Move: ")
            else:
                print("X's Turn!")
                piece = "X"
                move = input("Move: ")

            move = move.split(" ")

            self.takeSpace(piece,move[0], move[1])
            turn += 1
        self.showBoard()
        print("END GAME")

    #evaluation function made with help from https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/
    #O is max-ing, X is min-ing
    def evaluate(self):

        # Checking for Rows for X or O victory.
        for row in range(3):
            if (self.board[row][0] == self.board[row][1] and self.board[row][1] == self.board[row][2]):
                if (self.board[row][0] == "O"):
                    return 10
                elif (self.board[row][0] == "X"):
                    return -10

        # Checking for Columns for X or O victory.
        for col in range(3):

            if (self.board[0][col] == self.board[1][col] and self.board[1][col] == self.board[2][col]):

                if (self.board[0][col] == "O"):
                    return 10
                elif (self.board[0][col] == "X"):
                    return -10

        # Checking for Diagonals for X or O victory.
        if (self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]):

            if (self.board[0][0] == "O"):
                return 10
            elif (self.board[0][0] == "X"):
                return -10

        if (self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]):

            if (self.board[0][2] == "O"):
                return 10
            elif (self.board[0][2] == "X"):
                return -10

        # Else if none of them have won then return 0
        return 0

game = tictactoe()
game.playGame()
