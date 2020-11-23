class Game_Tutorial:
    WHITE = "w"
    BLACK = "b"
    EMPTY = "."
    size = 19

    def __init__(self):
        self.playerColour = self.BLACK
        self.computerColour = self.WHITE
        self.gameBoard = [
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
        ]

    def board(self):
        return self.gameBoard

    def result(self, move):
        x = move[0] - 1
        y = move[1] - 1
        self.gameBoard[x][y] = "b"

        # Win check
        for i in range(15):
            for j in range(15):
                # Horizontal win check
                if self.gameBoard[i][j] == 'b':
                    if self.gameBoard[i][j + 1] == 'b':
                        if self.gameBoard[i][j + 2] == 'b':
                            if self.gameBoard[i][j + 3] == 'b':
                                if self.gameBoard[i][j + 4] == 'b':
                                    return "Player"

                # Vertical win check
                if self.gameBoard[i][j] == 'b':
                    if self.gameBoard[i + 1][j] == 'b':
                        if self.gameBoard[i + 2][j] == 'b':
                            if self.gameBoard[i + 3][j] == 'b':
                                if self.gameBoard[i + 4][j] == 'b':
                                    return "Player"

                # Diagonal win check
                # down and right???
                if self.gameBoard[i][j] == 'b':
                    if self.gameBoard[i + 1][j + 1] == 'b':
                        if self.gameBoard[i + 2][j + 2] == 'b':
                            if self.gameBoard[i + 3][j + 3] == 'b':
                                if self.gameBoard[i + 4][j + 4] == 'b':
                                    return "Player"

                # up and right
                if i >= 4:
                    if self.gameBoard[i][j] == 'b':
                        if self.gameBoard[i - 1][j + 1] == 'b':
                            if self.gameBoard[i - 2][j + 2] == 'b':
                                if self.gameBoard[i - 3][j + 3] == 'b':
                                    if self.gameBoard[i - 4][j + 4] == 'b':
                                        return "Player"

                # down and left check for edge cases where up and right doesnt check
                if i >= 4 and j >= 4:
                    if self.gameBoard[i][j] == 'w':
                        if self.gameBoard[i + 1][j - 1] == 'w':
                            if self.gameBoard[i + 2][j - 2] == 'w':
                                if self.gameBoard[i + 3][j - 3] == 'w':
                                    if self.gameBoard[i + 4][j - 4] == 'w':
                                        return "Player"

        filled = 0
        for i in range(len(self.gameBoard)):
            for j in range(len(self.gameBoard[i])):
                if self.gameBoard[i][j] == '.':
                    filled += 1

        if filled == 361:
            return "Draw"

        # Almost loss warning check
        for i in range(16):
            for j in range(16):
                # Horizontal win check
                if self.gameBoard[i][j] == 'w':
                    if self.gameBoard[i][j + 1] == 'w':
                        if self.gameBoard[i][j + 2] == 'w':
                            if self.gameBoard[i][j + 3] == 'w':
                                print("horizontal win")  # Replace with warning display
                # Vertical win check
                if self.gameBoard[i][j] == 'w':
                    if self.gameBoard[i + 1][j] == 'w':
                        if self.gameBoard[i + 2][j] == 'w':
                            if self.gameBoard[i + 3][j] == 'w':
                                print("Vertical win")  # Replace with warning display
                # Diagonal win check
                # down and right???
                if self.gameBoard[i][j] == 'w':
                    if self.gameBoard[i + 1][j + 1] == 'w':
                        if self.gameBoard[i + 2][j + 2] == 'w':
                            if self.gameBoard[i + 3][j + 3] == 'w':
                                print("Diagonal win")  # Replace with warning display
                # up and right
                if i >= 3:
                    if self.gameBoard[i][j] == 'w':
                        if self.gameBoard[i - 1][j + 1] == 'w':
                            if self.gameBoard[i - 2][j + 2] == 'w':
                                if self.gameBoard[i - 3][j + 3] == 'w':
                                    print("Diagonal win also")  # Replace with warning display
                # down and left check for edge cases where up and right doesnt check
                if i >= 3 and j >= 3:
                    if self.gameBoard[i][j] == 'w':
                        if self.gameBoard[i + 1][j - 1] == 'w':
                            if self.gameBoard[i + 2][j - 2] == 'w':
                                if self.gameBoard[i + 3][j - 3] == 'w':
                                    print("Diagonal win also also")  # Replace with warning display

        bestMove = [
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ]

        blockPlayerBoard = [
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]

        for i in range(len(self.gameBoard)):
            for j in range(len(self.gameBoard[i])):
                points = [0, 0, 0, 0, 0, 0, 0, 0]

                stop = False
                horRightMove = j + 1
                while horRightMove < 19 and stop != True and points[0] < 5 and self.gameBoard[i][horRightMove] == "b":
                    points[0] += 1
                    if self.gameBoard[i][horRightMove] == "w":
                        stop = True
                    horRightMove += 1

                stop = False
                horLeftMove = j - 1
                while horLeftMove >= 0 and stop != True and points[1] < 5 and self.gameBoard[i][horLeftMove] == "b":
                    points[1] += 1
                    if self.gameBoard[i][horLeftMove] == "w":
                        stop = True
                    horLeftMove -= 1

                stop = False
                verTopMove = i - 1
                while verTopMove >= 0 and stop != True and points[2] < 5 and self.gameBoard[verTopMove][j] == "b":
                    points[2] += 1
                    if self.gameBoard[verTopMove][j] == "w":
                        stop = True
                    verTopMove -= 1

                stop = False
                verBottomMove = i + 1
                while verBottomMove < 19 and stop != True and points[3] < 5 and self.gameBoard[verBottomMove][j] == "b":
                    points[3] += 1
                    if self.gameBoard[verBottomMove][j] == "w":
                        stop = True
                    verBottomMove += 1

                stop = False
                diaTopRightX = i - 1
                diaTopRightY = j + 1
                while diaTopRightX >= 0 and diaTopRightY < 19 and stop != True and points[4] < 5 and \
                        self.gameBoard[diaTopRightX][diaTopRightY] == "b":
                    points[4] += 1
                    if self.gameBoard[diaTopRightX][diaTopRightY] == "w":
                        stop = True
                    diaTopRightX -= 1
                    diaTopRightY += 1

                stop = False
                diaTopLeftX = i - 1
                diaTopLeftY = j - 1
                while diaTopLeftX >= 0 and diaTopLeftY >= 0 and stop != True and points[5] < 5 and \
                        self.gameBoard[diaTopLeftX][diaTopLeftY] == "b":
                    points[5] += 1
                    if self.gameBoard[diaTopLeftX][diaTopLeftY] == "w":
                        stop = True
                    diaTopLeftX -= 1
                    diaTopLeftY -= 1

                stop = False
                diaBottomRightX = i + 1
                diaBottomRightY = j + 1
                while diaBottomRightX < 19 and diaBottomRightY < 19 and stop != True and points[6] < 5 and \
                        self.gameBoard[diaBottomRightX][diaBottomRightY] == "b":
                    points[6] += 1
                    if self.gameBoard[diaBottomRightX][diaBottomRightY] == "w":
                        stop = True
                    diaBottomRightX += 1
                    diaBottomRightY += 1

                stop = False
                diaBottomLeftX = i + 1
                diaBottomLeftY = j - 1
                while diaBottomLeftX < 19 and diaBottomLeftY >= 0 and stop != True and points[7] < 5 and \
                        self.gameBoard[diaBottomLeftX][diaBottomLeftY] == "b":
                    points[7] += 1
                    if self.gameBoard[diaBottomLeftX][diaBottomLeftY] == "w":
                        stop = True
                    diaBottomLeftX += 1
                    diaBottomLeftY -= 1

                blockPlayerBoard[i][j] = str(max(points))

        bestScore = 0
        bestPos = []
        for x in range(len(blockPlayerBoard)):
            for y in range(len(blockPlayerBoard[x])):
                if int(blockPlayerBoard[x][y]) >= bestScore and self.gameBoard[x][y] != "b" and self.gameBoard[x][
                    y] != "w":
                    bestScore = int(blockPlayerBoard[x][y])
                    bestPos = [x, y]

        if bestScore == 4:
            self.gameBoard[bestPos[0]][bestPos[1]] = "w"
            print("Blocked")
            print('\n'.join(map(''.join, self.gameBoard)))
            return "None"

        for i in range(len(self.gameBoard)):
            for j in range(len(self.gameBoard[i])):
                points = [0, 0, 0, 0, 0, 0, 0, 0]

                stop = False
                horRightMove = j + 1
                while horRightMove < 19 and stop != True and points[0] < 5 and self.gameBoard[i][horRightMove] == "w":
                    points[0] += 1
                    if self.gameBoard[i][horRightMove] == "b":
                        stop = True
                    horRightMove += 1

                stop = False
                horLeftMove = j - 1
                while horLeftMove >= 0 and stop != True and points[1] < 5 and self.gameBoard[i][horLeftMove] == "w":
                    points[1] += 1
                    if self.gameBoard[i][horLeftMove] == "b":
                        stop = True
                    horLeftMove -= 1

                stop = False
                verTopMove = i - 1
                while verTopMove >= 0 and stop != True and points[2] < 5 and self.gameBoard[verTopMove][j] == "w":
                    points[2] += 1
                    if self.gameBoard[verTopMove][j] == "b":
                        stop = True
                    verTopMove -= 1

                stop = False
                verBottomMove = i + 1
                while verBottomMove < 19 and stop != True and points[3] < 5 and self.gameBoard[verBottomMove][j] == "w":
                    points[3] += 1
                    if self.gameBoard[verBottomMove][j] == "b":
                        stop = True
                    verBottomMove += 1

                stop = False
                diaTopRightX = i - 1
                diaTopRightY = j + 1
                while diaTopRightX >= 0 and diaTopRightY < 19 and stop != True and points[4] < 5 and \
                        self.gameBoard[diaTopRightX][diaTopRightY] == "w":
                    points[4] += 1
                    if self.gameBoard[diaTopRightX][diaTopRightY] == "b":
                        stop = True
                    diaTopRightX -= 1
                    diaTopRightY += 1

                stop = False
                diaTopLeftX = i - 1
                diaTopLeftY = j - 1
                while diaTopLeftX >= 0 and diaTopLeftY >= 0 and stop != True and points[5] < 5 and \
                        self.gameBoard[diaTopLeftX][diaTopLeftY] == "w":
                    points[5] += 1
                    if self.gameBoard[diaTopLeftX][diaTopLeftY] == "b":
                        stop = True
                    diaTopLeftX -= 1
                    diaTopLeftY -= 1

                stop = False
                diaBottomRightX = i + 1
                diaBottomRightY = j + 1
                while diaBottomRightX < 19 and diaBottomRightY < 19 and stop != True and points[6] < 5 and \
                        self.gameBoard[diaBottomRightX][diaBottomRightY] == "w":
                    points[6] += 1
                    if self.gameBoard[diaBottomRightX][diaBottomRightY] == "b":
                        stop = True
                    diaBottomRightX += 1
                    diaBottomRightY += 1

                stop = False
                diaBottomLeftX = i + 1
                diaBottomLeftY = j - 1
                while diaBottomLeftX < 19 and diaBottomLeftY >= 0 and stop != True and points[7] < 5 and \
                        self.gameBoard[diaBottomLeftX][diaBottomLeftY] == "w":
                    points[7] += 1
                    if self.gameBoard[diaBottomLeftX][diaBottomLeftY] == "b":
                        stop = True
                    diaBottomLeftX += 1
                    diaBottomLeftY -= 1

                bestMove[i][j] = str(max(points))

        bestScore = 0
        bestPos = []
        for x in range(len(bestMove)):
            for y in range(len(bestMove[x])):
                if int(bestMove[x][y]) >= bestScore and self.gameBoard[x][y] != "b" and self.gameBoard[x][y] != "w":
                    bestScore = int(bestMove[x][y])
                    bestPos = [x, y]

        self.gameBoard[bestPos[0]][bestPos[1]] = "w"

        if bestScore == 4:
            # print("Bot")
            returnList = []
            returnList.append("Bot")
            returnList.append(self.gameBoard)
            return ("Bot")
            print('\n'.join(map(''.join, self.gameBoard)))
        else:
            return ("None")

        print('\n'.join(map(''.join, self.gameBoard)))