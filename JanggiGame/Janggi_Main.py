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
    game_state = Janggi_Engine.JanggiGameState()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    load_assets()  # only load once

    # drawBoard(screen)


    # board = game_state.get_board()

    game_executing = True
    active_square = () #nothing selected to start
    input_clicks = [] #keep track of ticks
    row = -1
    col = -1
    board_row = -1
    board_col = -1
    x_offset = 75
    y_offset = 75
    row_translation = {
        1: [75,125],
        2: [150,200],
        3: [225,275],
        4: [300,350],
        5: [375,425],
        6: [450,500],
        7: [525,575],
        8: [600,650],
        9: [675,725],
        10: [750,800]
    }
    col_translation = {
        1: [75,125],
        2: [150, 200],
        3: [225, 275],
        4: [300, 350],
        5: [375, 425],
        6: [450, 500],
        7: [525, 575],
        8: [600,650],
        9: [675,725]
    }

    while game_executing:
        for eve in pygame.event.get():
            if eve.type == pygame.QUIT:
                game_executing = False
            elif eve.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos() # x,y of mouse
                row = location[1]
                col = location[0]


                if row > row_translation[1][0] and row < row_translation[1][1]:
                    board_row = '1'
                    row = 1
                elif row > row_translation[2][0] and row < row_translation[2][1]:
                    board_row = '2'
                    row = 2
                elif row > row_translation[3][0] and row < row_translation[3][1]:
                    board_row = '3'
                    row = 3
                elif row > row_translation[4][0] and row < row_translation[4][1]:
                    board_row = '4'
                    row = 4
                elif row > row_translation[5][0] and row < row_translation[5][1]:
                    board_row = '5'
                    row = 5
                elif row > row_translation[6][0] and row < row_translation[6][1]:
                    board_row = '6'
                    row = 6
                elif row > row_translation[7][0] and row < row_translation[7][1]:
                    board_row = '7'
                    row = 7
                elif row > row_translation[8][0] and row < row_translation[8][1]:
                    board_row = '8'
                    row = 8
                elif row > row_translation[9][0] and row < row_translation[9][1]:
                    board_row = '9'
                    row = 9
                elif row > row_translation[10][0] and row < row_translation[10][1]:
                    board_row = '10'
                    row = 10

                if col > col_translation[1][0] and col < col_translation[1][1]:
                    board_col = 'a'
                    col = 1
                elif col > col_translation[2][0] and col < col_translation[2][1]:
                    board_col = 'b'
                    col = 2
                elif col > col_translation[3][0] and col < col_translation[3][1]:
                    board_col = 'c'
                    col = 3
                elif col > col_translation[4][0] and col < col_translation[4][1]:
                    board_col = 'd'
                    col = 4
                elif col > col_translation[5][0] and col < col_translation[5][1]:
                    board_col = 'e'
                    col = 5
                elif col > col_translation[6][0] and col < col_translation[6][1]:
                    board_col = 'f'
                    col = 6
                elif col > col_translation[7][0] and col < col_translation[7][1]:
                    board_col = 'g'
                    col = 7
                elif col > col_translation[8][0] and col < col_translation[8][1]:
                    board_col = 'h'
                    col = 8
                elif col > col_translation[9][0] and col < col_translation[9][1]:
                    board_col = 'i'
                    col = 9

                if active_square == (board_col+board_row): #user clicked same square twice
                #     #pass your turn
                     game_state.make_move(input_clicks[0], input_clicks[0])
                     active_square = () #deselect
                     input_clicks = [] #clear click log
                elif row > 0 and row < 11 and col > 0 and col < 10:
                     active_square = (board_col+board_row)
                     input_clicks.append(active_square) #append both first and second clicks
                else:
                     active_square = ()  # deselect
                     input_clicks = []  # clear click log
                #was this the second click?
                if len(input_clicks) == 2:  # second click
                     print(input_clicks[0]+input_clicks[1])
                     print(game_state.make_move(str(input_clicks[0]), str(input_clicks[1])))
                     game_state.print_board()
                     active_square = ()
                     input_clicks = []


        drawGame(screen, game_state, row, col)
        # game_state.print_board()
        clock.tick(MAX_FPS)
        pygame.display.flip()


def drawGame(screen, game_state, row, col):
    '''draw board and pieces'''
    drawBoard(screen)
    drawPieces(screen, game_state)

    # draw turn
    turn = game_state.get_turn()
    if turn == "r":
        turn = "Red"
    else:
        turn = "Blue"
    font = pygame.font.SysFont(None, 32)
    text = font.render("Turn: ", True, "black")
    text_2 = font.render(turn, True, turn)
    screen.blit(text, (30,30))
    screen.blit(text_2, (90,30))

    font_2 = pygame.font.SysFont(None, 32)
    text_3 = font_2.render(str(row), True, "black")
    text_4 = font_2.render(str(col), True, "black")
    screen.blit(text_3, (200, 30))
    screen.blit(text_4, (300, 30))



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


