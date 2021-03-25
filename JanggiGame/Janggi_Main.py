'''
Display game state, capture user input
'''

import pygame
from JanggiGame import Janggi_Engine
from JanggiGame import Janggi_Pieces


# pygame.init() if there is an error load_assets tries to load first, then init sooner
WIDTH = 800
HEIGHT = 875
DIM_X = 9
DIM_Y = 10
SQ_SIZE = 50
MAX_FPS = 15

IMAGES = {}

'''
Load Assets
'''

def load_assets():
    '''load images'''
    visual_pieces = [
        'rCt',
        'rEl',
        'rHs',
        'rGd',
        'rGn',
        'rCn',
        'rSd',
        'bCt',
        'bEl',
        'bHs',
        'bGd',
        'bGn',
        'bCn',
        'bSd',
    ]
    for piece in visual_pieces:
        IMAGES[piece] = pygame.transform.scale((pygame.image.load("assets/" + piece + ".png")), (SQ_SIZE, SQ_SIZE))


'''
User input, visual output
'''

def main():
    '''main pygame loop'''
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    load_assets()  # only load once

    # drawBoard(screen)

    game_state = Janggi_Engine.JanggiGameState()
    # board = game_state.get_board()

    game_executing = True
    while game_executing:
        for eve in pygame.event.get():
            if eve.type == pygame.QUIT:
                game_executing = False
        drawGame(screen, game_state)
        clock.tick(MAX_FPS)
        pygame.display.flip()


def drawGame(screen, game_state):
    '''draw board and pieces'''
    drawBoard(screen)
    drawPieces(screen, game_state)

def drawBoard(screen):
    '''draw background color, board, and lines'''

    # load background image
    background_image = pygame.image.load("assets/visual_board.png")
    # fill background
    screen.fill((89,58,27))

    # draw lines
    x_1 = 75
    y_1 = 75
    x_2 = 675
    y_2 = 75

    # draw rows
    for i in range (10):
        pygame.draw.line(background_image, "black", (x_1, y_1), (x_2, y_2), width=2)
        y_1 += 75
        y_2 += 75

    x_1 = 75
    y_1 = 75
    x_2 = 75
    y_2 = 750

    # draw cols
    for i in range (9):
        pygame.draw.line(background_image, "black", (x_1, y_1), (x_2, y_2), width=2)
        x_1 += 75
        x_2 += 75

    # draw red palace

    x_1 = 300
    y_1 = 75
    x_2 = 450
    y_2 = 225

    pygame.draw.line(background_image, "black", (x_1, y_1), (x_2, y_2), width=3)

    x_1 = 450
    y_1 = 75
    x_2 = 300
    y_2 = 225

    pygame.draw.line(background_image, "black", (x_1, y_1), (x_2, y_2), width=3)

    # draw blue palace

    x_1 = 300
    y_1 = 600
    x_2 = 450
    y_2 = 750

    pygame.draw.line(background_image, "black", (x_1, y_1), (x_2, y_2), width=3)

    x_1 = 450
    y_1 = 600
    x_2 = 300
    y_2 = 750

    pygame.draw.line(background_image, "black", (x_1, y_1), (x_2, y_2), width=3)

    # display background, offset by 25
    screen.blit(background_image, [25, 25])


def drawPieces(screen, game_state):
    for row in range(1, 11, 1):
        for col in range(0, 9, 1):
            piece = game_state.get_piece(row, col)
            if piece != None:
                piece_name = piece.get_team() + piece.get_name()
                screen.blit(IMAGES[piece_name], pygame.Rect((col*75)+75, (row*75), SQ_SIZE, SQ_SIZE))




if  __name__ == '__main__':
    main()