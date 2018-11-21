import random, sys, pygame, time, copy
from pygame.locals import *


FPS = 60 # 초당프레임
width = 640
height = 320
spacesize = 50
boardwidth =  8
boardheight = 8
WHITE_TILE = 'WHITE_TILE'
BLACK_TILE = 'BLACK_TILE'
EMPTY_SPACE = 'EMPTY_SPACE'
HINT_TILE = 'HINT_TILE'
animation = 25

Xmargin = int((width - (boardwidth*spacesize)))
Ymargin = int((height - (boardwidth*spacesize)))

WHITE = (255,255,255) #RGB
BLACK = (  0,  0,  0)
BIOLET = (  121,  21,  110)
APRICOT = (  255,  193,  158)
BRIGHTBLUE = (  0,  50,  225)

Textcolor1 = APRICOT
Textcolor2 = BRIGHTBLUE
GRIDLINE = BLACK
Textcolor = WHITE
Hintcolor = BIOLET

def main():
    global MAINCLOCK, DISPLAYSURF, FONT, BIGFONT, BGIMAGE, PLAYER, COMPUTER

    pygame.init()
    MAINCLOCK = pygame.time.Clock() #초당 프레임을 위한 설정
    DISPLAYSURF = pygame.display.set_mode((width,height))
    pygame.display.set_caption('HellOthello')
    FONT = pygame.font.Font('Inkfree.ttf',16)
    BIGFONT = pygame.font.Font('Inkfree.ttf',32)

    boardimage = pygame.image.load('board.jpg') #보드 밑판
    boardimage = pygame.transform.smoothscale(boardimage, (boardwidth*spacesize,boardheight*spacesize))
    boardimageRect = boardimage.get_rect()
    BGIMAGE = pygame.image.load('background.jpg')
    BGIMAGE = pygame.transform.smoothscale(BGIMAGE,(width,height))
    BGIMAGE.blit(boardimage,boardimageRect)


    while True:
        if runGame() == False:
            break

def runGame():
    mainboard = getNewBoard()
    resetBoard(mainboard)
    showHINT = False
    turn = random.choice(['computer','player'])

    drawBoard(mainboard)
    playerTile, computerTile = enterPlayerTile()

    newGameSurf = FONT.render('New Game', True, Textcolor, Textcolor2)
    newGameRect = newGameSurf.get_rect()
    newGameRect.topright = (width - 8 , 10)
    hintSurf = FONT.render('Hints', True, Hintcolor,Textcolor2)
    hintRect = hintSurf.get_rect()
    hintRect.topright = (width -8, 40)

    while True: #메인루프
        if turn == 'player':
            if getVaildMoves(mainboard, playerTile)==[]:
                break
            movexy = None
            while movexy == None:

                if showHINT:
                    boardToDraw = getBoardWithValidMoves(mainboard, playerTile)
                else:
                    boardToDraw = mainboard
                checkForQuit()
                for event in pygame.event.get():
                    if event. type == MOUSEBUTTONUP:
                        mousex, mousey = event.pos
                        if newGameRect.collidepoint((mousex,mousey)):
                            return True
                        elif hintRect.collidepoint((mousex,mousey)):
                            showHINT = not showHINT

                        movesy = getSpaceClicked(mousex,mousey)
                        if movexy != None and not isValidMove(mainboard, playerTile, movexy[0], movexy[1]):
                            movexy = None

                #게임보드 그리기
                drawBoard(boardToDraw)
                drawInfo(boardToDraw,playerTile,computerTile,turn)

                #새게임과 힌트버튼 그리기
                DISPLAYSURF.blit(newGameSurf,newGameRect)
                DISPLAYSURF.blit(hintSurf,hintRect)

                MAINCLOCK.tick(FPS)
                pygame.display.update()

            makeMove(mainboard,playerTile,movexy[0],movexy[1],True)
            if getVaildMoves(mainboard, computerTile) !=[]:
                turn = 'computer'
        else:
            #컴퓨터의 턴이지만 움직일 수 있는 돌이 없을 때
            if getVaildMoves(mainboard,computerTile) == []:
                break

            #보드 그리기
            drawBoard(mainboard)
            drawInfo(mainboard,playerTile,computerTile,turn)

            DISPLAYSURF.blit(newGameSurf, newGameRect)
            DISPLAYSURF.blit(hintSurf,hintRect)

            x , y = getComputerMove(mainboard,computerTile)
            makeMove(mainboard,computerTile,x,y,True)
            if getVaildMoves(mainboard, playerTile) != []:
                turn = 'player'

            drawBoard(mainboard)
            scores = getScoreOfBoard(mainboard)

            if scores[playerTile] > scores[computerTile]:
                text = '컴퓨터를 이겼습니다!'
            elif scores[playerTile] < scores[computerTile]:
                text = '컴퓨터에게 졌습니다!'
            else:
                text = '비겼습니다!'

            textSurf = FONT.render(text,True,Textcolor,Textcolor1)
            textRect = textSurf.get_rect()
            textRect.center = (int(width/2), int(height/2))
            DISPLAYSURF.blit(textSurf, textRect)

            text2Surf = BIGFONT.render('Play Again?',True,Textcolor,Textcolor2)
            text2Rect =  text2Surf.get_rect()
            text2Rect.center = (int(width/2), int(height/2)+50)

            yesSurf = BIGFONT.render('yes', True, Textcolor, Textcolor1)
            yesRect = yesSurf.get_rect()
            yesRect.center = (int(width/2)-60, int(height/2)+90)

            noSurf = BIGFONT.render('No',True,Textcolor,Textcolor1)
            noRect = noSurf.get_rect()
            noRect.center = (int(width/2)+60, int(height/2)+90)

            while True:
                # 네, 아니오 버튼 처리
                checkForQuit()
                for event in pygame.event.get(): #이벤트 헨들링 루프
                    if event.type == MOUSEBUTTONUP:
                        mousex, mousey = event.pos
                        if yesRect.collidepoint( (mousex,mousey) ):
                            return True
                        elif noRect.collidepoint( (mousex, mousey) ):
                            return False
                DISPLAYSURF.blit(textSurf,textRect)
                DISPLAYSURF.blit(text2Surf, text2Rect)
                DISPLAYSURF.blit(yesSurf, yesRect)
                DISPLAYSURF.blit(noSurf, noRect)
                pygame.display.update()
                MAINCLOCK.tick(FPS)

def translateBoardToPixelcoord(x,y):
    return Xmargin + x*spacesize + int(spacesize/2), Ymargin + y * spacesize + int(spacesize/2)

def animatateTilechange(tilesToFlip,tileColor, additionalTile):
    if tileColor == WHITE_TILE:
        additionalTileColor = WHITE
    else:
        additionalTileColor = BLACK
    additionalTileX, additionalTileY = translateBoardToPixelcoord(additionalTile[0],additionalTile[1])
    pygame.draw.circle(DISPLAYSURF, additionalTileColor,(additionalTileX,additionalTileY), int(spacesize/2)-4)
    pygame. display. update()

    for rgbValues in range (0,255, int(animation * 2.55)):
        if rgbValues >255:
            rgbValues = 255
        elif rgbValues < 0:
            rgbValues = 0

        if tileColor == WHITE_TILE:
            color = tuple([255-rgbValues] *3)
        elif tileColor == BLACK_TILE:
            color = tuple([255 - rgbValues]*3)

        for x,y in tilesToFlip:
            centerx,centery = translateBoardToPixelcoord(x,y)
            pygame.draw.circle(DISPLAYSURF, color, (centerx,centery), int(spacesize/2)-4)
            pygame.display.update()
            MAINCLOCK.tick(FPS)
            checkForQuit()

def drawBoard(board):
    DISPLAYSURF.blit(BGIMAGE, BGIMAGE.get_rect())
    for x in range (boardwidth +1):
        startx = (x*spacesize) + Xmargin
        starty = Ymargin
        endx = Xmargin + (boardwidth * spacesize)
        endy = Ymargin + (boardwidth*spacesize)
        pygame.draw.line(DISPLAYSURF,GRIDLINE, (startx, starty), (endx, endy))

        for x in range (boardwidth):
            for y in range (boardheight):
                centerx, centery = translateBoardToPixelcoord(x,y)
                if board[x][y]==WHITE_TILE or board[x][y]==BLACK_TILE:
                    if board[x][y] == WHITE_TILE:
                        tileColor = WHITE
                    else:
                        tileColor = BLACK
                    pygame.draw.circle(DISPLAYSURF, tileColor, (centerx,centery), int(spacesize/2)-4)
                if board[x][y] == HINT_TILE:
                    pygame.draw.rect(DISPLAYSURF, Hintcolor, (centerx -4, centery -4), 8, 8)

def getSpaceClicked(mousex,mousey):
    for x in range(boardwidth):
        for y in range(boardheight):
            if mousex > x*spacesize + Xmargin and \
               mousex < (x+1) * spacesize + Xmargin and \
               mousey > y * spacesize + Ymargin and \
               mousey < (y + 1) * spacesize + Ymargin:
                return (x,y)
    return None

def drawInfo(board, playerTile, computerTile, turn):

    scores = getScoreOfBoard(board)
    scoreSurf = FONT.render("player point: %s   computer point: %s " % (str(scores[playerTile]),str(scores[computerTile], True, Textcolor)))
    scoreRect = scoreSurf.get_rect()
    scoreRect.bottoleft = (10, height - 5)
    DISPLAYSURF.blit(scoreSurf,scoreRect)

def resetBoard(board):
    for x in range(boardwidth):
        for y in range(boardheight):
            board[x][y] = EMPTY_SPACE

    board [3][3] = WHITE_TILE
    board [3][4] = BLACK_TILE
    board [4][3] = BLACK_TILE
    board [4][4] = WHITE_TILE

def getNewBoard():
    board = []
    for i in range(boardwidth):
        board.append([EMPTY_SPACE] * boardheight)

    return board

def isValidMove(board, tile, xstart, ystart):
    if board[xstart][ystart] != EMPTY_SPACE or not isOnBoard(xstart,ystart):
        return False

    board[xstart][ystart] = tile
    if tile == WHITE_TILE:
        otherTile = BLACK_TILE
    else:
        otherTile = WHITE_TILE
        TileToFlip = []

        for xdirection, ydirection in [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]:
            x,y = xstart, ystart

            x += xdirection
            y += ydirection
            if isOnBoard(x,y) and board[x][y] == otherTile:
                if not isOnBoard(x,y):
                    break
            if not isOnBoard(x,y):
                continue
            if board[x][y] == tile:
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tileToFlip.append([x,y])
        board[xstart][ystart] = EMPTY_SPACE
        if len(tileToFlip) == 0:
            return False
        return tileToFlip
def isOnBoard(x,y):
    return x >=0 and x < boardwidth and y >= 0 and y <boardheight

def getBoardWithValidMoves(board,tile):
    dupeBoard = copy.deepcopy(board)
    for x,y in getVaildMoves(dupeBoard, tile):
        dupeBoard[x][y] = HINT_TILE
    return dupeBoard

def getVaildMoves(board, tile):
    validMoves = []

    for x in range (boardwidth):
        for y in range (boardheight):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append((x,y))
    return validMoves

def getScoreOfBoard(board):

    xscore = 0
    oscore = 0
    for x in range(boardwidth):
        for y in range(boardheight):
            if board[x][y] == WHITE_TILE:
                xscore +=1
            if board[x][y] == BLACK_TILE:
                oscore +=1
    return {WHITE_TILE:xscore, BLACK_TILE:oscore}

def enterPlayerTile():
    textSurf = FONT.render('White or Black?', True, Textcolor, Textcolor1)
    textRect = textSurf.get_rect()
    textRect.center = (int(width/2), int(height/2))

    xSurf = BIGFONT.render('흰색',True, Textcolor,Textcolor1)
    xRect = xSurf.get_rect()
    xRect.center = (int(width/2) - 60, int(height/2)+40)

    oSurf = BIGFONT.render('검정', True, Textcolor,Textcolor1)
    oRect = oSurf.get_rect()
    oRect.center = (int(width/2)+60 , int(height/2)+40)

    while True:
        checkForQuit()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                if xRect.collidepoint( (mousex,mousey) ):
                    return [WHITE_TILE, BLACK_TILE]
                elif oRect.collidepoint( (mousex,mousey) ):
                    return [BLACK_TILE,WHITE_TILE]

        DISPLAYSURF.blit(textSurf,textRect)
        DISPLAYSURF.blit(xSurf,xRect)
        DISPLAYSURF.blit(oSurf, oRect)
        pygame.display.update()
        MAINCLOCK.tick(FPS)

def makeMove(board, tile, xstart, ystart, realMove=False):
    tileToFlip = isValidMove(board, tile, xstart, ystart)

    if tileToFlip == False:
        return False

    board[xstart][ystart] = tile
    if realMove:
        animatateTilechange(tilesToFlip, tile, (xstart,ystart))

    for x,y in tileToFlip:
        board[x][y] = tile
    return True

def isOnCorner(x,y):
    return (x==0 and y==o) or \
           (x==boardwidth and y==0)or\
           (x == 0 and y == boardheight)or\
           (x==boardwidth and y ==boardheight)

def getComputerMove(board, computerTile):
    possibleMoves = getVaildMoves(board, computerTile)
    random.shuffle(possibleMoves)
    for x,y in possibleMoves:
        if isOnCorner(x,y):
            return [x,y]
    bestScore = -1
    for x,y in possibleMoves:
        dupeBoard = copy.deepcopy(board)
        makeMove(dupeBoard, computerTile,x,y)
        score = getScoreOfBoard(dupeBoard)[computerTile]
        if score> bestScore:
            bestScore = score
    return bestMove

def checkForQuit():
    for event in pygame.event.get((QUIT, KEYUP)):
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):

            pygame.quit()
            sys.exit()

main()
