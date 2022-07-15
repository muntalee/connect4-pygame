import pygame
pygame.init()

# 0 = empty
# 1 = red
# 2 = yellow
# board[y][x]

board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

# Starter items
size = (700, 600)
window = pygame.display.set_mode(size)
pygame.display.set_caption("Programming Club's Connect 4")
window.fill((255, 255, 255))

# Assets
board_image = pygame.image.load("assets/board.png")
red_original = pygame.image.load("assets/red.png")
red_piece = pygame.transform.scale(red_original, (100, 100))
yellow_original = pygame.image.load("assets/yellow.png")
yellow_piece = pygame.transform.scale(yellow_original, (100, 100))
window.blit(board_image, (0, 0))


# Update the board based on the array
def updateBoard():
    for i in range(len(board[0])):
        for j in range(len(board)):
            if board[j][i] == 1:
                window.blit(red_piece, (i*100, j*100))
            if board[j][i] == 2:
                window.blit(yellow_piece, (i*100, j*100))
    window.blit(board_image, (0, 0))


# Prints the board
def printBoard():
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=" ")
        print()


# Place the piece in the board array
def placePiece(col, piece):
    if board[0][col] == 1 or board[0][col] == 2:
        return
    for i in range(len(board)):
        if board[i][col] == 1 or board[i][col] == 2:
            board[i-1][col] = piece
            return
    board[5][col] = piece


# Placing piece by mouse
isPlayer1 = True


def placeByMouse(row):
    global isPlayer1
    if isPlayer1:
        placePiece(row, 1)
        if checkWin(1):
            pygame.display.set_caption("Player 1 Wins!")
            winner()
        else:
            updateBoard()
            isPlayer1 = False

    else:
        placePiece(row, 2)
        if checkWin(2):
            pygame.display.set_caption("Player 2 Wins!")
            winner()
        else:
            updateBoard()
            isPlayer1 = True


# Check if we won
def checkWin(p):
    # Horizontal
    for i in range(len(board[0])):
        for j in range(len(board)):
            try:
                if (board[i][j] == p and board[i][j+1] == p and board[i][j+2] == p and board[i][j+3] == p):
                    updateBoard()
                    x1 = (j*100) + 50
                    y1 = (i*100) + 50
                    x2 = ((j+3)*100) + 50
                    y2 = (i*100) + 50

                    pygame.draw.line(window, (0,0,0), (x1,y1), (x2,y2), width=10)
                    pygame.draw.circle(window, (0,0,0), (x1+1,y1+1), radius=5)
                    pygame.draw.circle(window, (0,0,0), (x2+1,y2+1), radius=5)
                    return True
            except:
                pass

    # Vertical
    for i in range(len(board[0])):
        for j in range(len(board)):
            try:
                if (board[i][j] == p and board[i+1][j] == p and board[i+2][j] == p and board[i+3][j] == p):
                    updateBoard()
                    x1 = (j*100) + 50
                    y1 = (i*100) + 50
                    x2 = (j*100) + 50
                    y2 = ((i+3)*100) + 50

                    pygame.draw.line(window, (0,0,0), (x1,y1), (x2,y2), width=10)
                    pygame.draw.circle(window, (0,0,0), (x1+1,y1+1), radius=5)
                    pygame.draw.circle(window, (0,0,0), (x2+1,y2+1), radius=5)
                    return True
            except:
                pass

    # Diagonal (going up)
    for i in range(len(board[0])):
        for j in range(len(board)):
            try:
                if (board[i][j] == p and board[i-1][j+1] == p and board[i-2][j+2] == p and board[i-3][j+3] == p):
                    updateBoard()
                    x1 = (j*100) + 50
                    y1 = (i*100) + 50
                    x2 = ((j+3)*100) + 50
                    y2 = ((i-3)*100) + 50

                    pygame.draw.line(window, (0,0,0), (x1,y1), (x2,y2), width=10)
                    pygame.draw.circle(window, (0,0,0), (x1+1,y1+1), radius=5)
                    pygame.draw.circle(window, (0,0,0), (x2+1,y2+1), radius=5)
                    return True
            except:
                pass

    # Diagonal (going down)
    for i in range(len(board[0])):
        for j in range(len(board)):
            try:
                if (board[i][j] == p and board[i+1][j+1] == p and board[i+2][j+2] == p and board[i+3][j+3] == p):
                    updateBoard()
                    x1 = (j*100) + 50
                    y1 = (i*100) + 50
                    x2 = ((j+3)*100) + 50
                    y2 = ((i+3)*100) + 50

                    pygame.draw.line(window, (0,0,0), (x1,y1), (x2,y2), width=10)
                    pygame.draw.circle(window, (0,0,0), (x1+1,y1+1), radius=5)
                    pygame.draw.circle(window, (0,0,0), (x2+1,y2+1), radius=5)
                    return True
            except:
                pass

    return False


def winner():
    pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)


updateBoard()

running = True

# Game Loop
while running:
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Gets the x and y position of mouse
        mouseX, mouseY = pygame.mouse.get_pos()

        # Checks if we clicked on the screen
        if event.type == pygame.MOUSEBUTTONDOWN:

            # Depending on our X value and the range, we place a piece
            if mouseX > 0 and mouseX < 100:
                placeByMouse(0)
            if mouseX > 100 and mouseX < 200:
                placeByMouse(1)
            if mouseX > 200 and mouseX < 300:
                placeByMouse(2)
            if mouseX > 300 and mouseX < 400:
                placeByMouse(3)
            if mouseX > 400 and mouseX < 500:
                placeByMouse(4)
            if mouseX > 500 and mouseX < 600:
                placeByMouse(5)
            if mouseX > 600 and mouseX < 700:
                placeByMouse(6)

    pygame.display.flip()

pygame.quit()
