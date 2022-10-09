# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class node:
    def __init__(self, value, listOfNexts, move):
        self.value = value
        self.next = listOfNexts
        self.move = move #[-1,-1] if current board

    def setNext(self, newBoard, move):
        self.next.append(node(newBoard, [], move))

class tree:

    def __init__(self, start):
        self.root = start


class tictactoe:

    def __init__(self):
        self.board = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
        self.bestState = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
        self.bestMove = [-1,-1]

    def setBoard(self, customBoard):
        self.board = customBoard

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

        #return 1 for O win, -1 for X win, 0 for tie, 2 for no win
        if won and winner == "O":
            return 1
        elif won and winner == "X":
            return -1
        elif tie:
            return 0
        else:
            return 2

    def showBoard(self, board):
        print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " ")
        print("---+---+---")
        print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " ")
        print("---+---+---")
        print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " ")

    def getMove(self, player, isAI):
        if isAI:
            depth = 0
            root = node(self.board, [], [-1, -1])
            self.stateTree(root, player)
            for eachRow in self.board:
                depth += eachRow.count(" ")
            bestEval = self.minimaxAlphaBeta(root, depth, -1000000, 10000000, player)  # returns eval and changes self.bestState and self.bestMove
            #bestEval = self.minimax(root, depth, player)  # returns eval and changes self.bestState and self.bestMove

            y = self.bestMove[0]
            x = self.bestMove[1]
            if y == 0:
                move = "top"
            elif y == 1:
                move = "middle"
            elif y == 2:
                move = "bottom"

            if x == 0:
                move += " left"
            elif x == 1:
                move += " middle"
            elif x == 2:
                move += " right"

            print("Move: " + move)
        else:
            move = input("Move: ")

        return move

    def playGame(self):
        turn = 0
        while(self.checkWin() == 2):
            self.showBoard(self.board)
            print("Board score: " ,self.evaluate(self.board))
            if turn % 2 == 0:
                print("O's Turn!")
                piece = "O"
                move = self.getMove("O", True)
            else:
                print("X's Turn!")
                piece = "X"
                move = self.getMove("X", False)


            move = move.split(" ")

            self.takeSpace(piece,move[0], move[1])
            turn += 1

        result = self.checkWin()
        if result == 1:
            print("O Wins!")
        elif result == -1:
            print("X Wins!")
        elif result == 0:
            print("It's a tie!")
        else:
            print("--ERROR--")
        self.showBoard(self.board)
        print("Board score: ", self.evaluate(self.board))
        print("END GAME")

    def getBoardCopy(self, board):
        newBoard = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
        for i in range(3):
            for j in range(3):
                newBoard[j][i] = board[j][i]
        return newBoard

    #evaluation function made with help from https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/
    #O is max-ing, X is min-ing
    def evaluate(self, board):
        score = 0
        # Checking for Rows for X or O victory.
        for row in range(3):
            if (board[row][0] == board[row][1] and board[row][1] == board[row][2]):
                if (board[row][0] == "O"):
                    score += 1000
                elif (board[row][0] == "X"):
                    score += -1000
            #check for near victory------------------------------
            if board[row][0] == board[row][1] and board[row][2] == " ":
                if (board[row][0] == "O"):
                    score += 10
                elif (board[row][0] == "X"):
                    score += -10

            if board[row][1] == board[row][2] and board[row][0] == " ":
                if (board[row][1] == "O"):
                    score += 10
                elif (board[row][1] == "X"):
                    score += -10

            if board[row][0] == board[row][2] and board[row][1] == " ":
                if (board[row][0] == "O"):
                    score += 10
                elif (board[row][0] == "X"):
                    score += -10
            #------------------------------------------
        # Checking for Columns for X or O victory.
        for col in range(3):

            if (board[0][col] == board[1][col] and board[1][col] == board[2][col]):

                if (board[0][col] == "O"):
                    score += 1000
                elif (board[0][col] == "X"):
                    score += -1000
            # check for near victory------------------------------
            if board[0][col] == board[1][col] and board[2][col] == " ":
                if (board[0][col] == "O"):
                    score += 10
                elif (board[0][col] == "X"):
                    score += -10

            if board[1][col] == board[2][col] and board[0][col] == " ":
                if (board[1][col] == "O"):
                    score += 10
                elif (board[1][col] == "X"):
                    score += -10

            if board[0][col] == board[2][col] and board[1][col] == " ":
                if (board[0][col] == "O"):
                    score += 10
                elif (board[0][col] == "X"):
                    score += -10
            # ------------------------------------------


        # Checking for Diagonals for X or O victory.
        if (board[0][0] == board[1][1] and board[1][1] == board[2][2]):

            if (board[0][0] == "O"):
                score += 1000
            elif (board[0][0] == "X"):
                score += -1000

        if (board[0][2] == board[1][1] and board[1][1] == board[2][0]):

            if (board[0][2] == "O"):
                score += 1000
            elif (board[0][2] == "X"):
                score += -1000

        # check for near victory------------------------------
        if board[0][0] == board[1][1] and board[2][2] == " ":
            if (board[0][0] == "O"):
                score += 10
            elif (board[0][0] == "X"):
                score += -10

        if board[1][1] == board[2][2] and board[0][0] == " ":
            if (board[1][1] == "O"):
                score += 10
            elif (board[1][1] == "X"):
                score += -10

        if board[0][0] == board[2][2] and board[1][1] == " ":
            if (board[0][0] == "O"):
                score += 10
            elif (board[0][0] == "X"):
                score += -10

        if board[0][2] == board[1][1] and board[2][0] == " ":
            if (board[0][2] == "O"):
                score += 10
            elif (board[0][2] == "X"):
                score += -10

        if board[1][1] == board[2][0] and board[0][2] == " ":
            if (board[1][1] == "O"):
                score += 10
            elif (board[1][1] == "X"):
                score += -10

        if board[0][2] == board[2][0] and board[1][1] == " ":
            if (board[0][2] == "O"):
                score += 10
            elif (board[0][2] == "X"):
                score += -10
        # ------------------------------------------

        # Else if none of them have won then score is 0
        return score

    def stateTree(self, currBoard, player):
        piece = player
        if player == "O":
            nextPlayer = "X"
        else:
            nextPlayer = "O"
        root = currBoard
        baseBoard = self.getBoardCopy(root.value)

        #base case --- end generation if win or tie
        ttt = tictactoe()
        ttt.setBoard(currBoard.value)
        if ttt.checkWin() != 2:
            return

        for i in range(3):
            for j in range(3):
                board = self.getBoardCopy(baseBoard)
                if baseBoard[j][i] == " ":
                    board[j][i] = piece
                    root.setNext(board, [j,i])

        #recursively generate each next game state
        for eachNext in root.next:
            self.stateTree(eachNext, nextPlayer)

    def minimax(self, state, depth, player):
        if player == "O":
            maxing = True
        else:
            maxing = False

        if depth == 0:
            self.bestState = state
            return self.evaluate(state.value)

        if maxing:
            maxEval = -100000
            for eachNextState in state.next:
                eval = self.minimax(eachNextState, depth-1, "X")
                maxEval = max(maxEval,eval)
                if maxEval == eval:
                    self.bestState = eachNextState
                    self.bestMove = eachNextState.move
            return maxEval
        else:
            minEval = 100000
            for eachNextState in state.next:
                eval = self.minimax(eachNextState, depth - 1, "O")
                minEval = min(minEval, eval)
                if minEval == eval:
                    self.bestState = eachNextState
                    self.bestMove = eachNextState.move
            return minEval

    def minimaxAlphaBeta(self, state, depth, alpha, beta, player):
        if player == "O":
            maxing = True
        else:
            maxing = False

        if depth == 0:
            self.bestState = state
            return self.evaluate(state.value)

        if maxing:
            maxEval = -100000
            for eachNextState in state.next:
                eval = self.minimaxAlphaBeta(eachNextState, depth-1, alpha, beta, "X")
                maxEval = max(maxEval,eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
                if maxEval == eval:
                    self.bestState = eachNextState
                    self.bestMove = eachNextState.move
            return maxEval
        else:
            minEval = 100000
            for eachNextState in state.next:
                eval = self.minimaxAlphaBeta(eachNextState, depth - 1, alpha, beta, "O")
                minEval = min(minEval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
                if minEval == eval:
                    self.bestState = eachNextState
                    self.bestMove = eachNextState.move
            return minEval






game = tictactoe()
game.playGame()
