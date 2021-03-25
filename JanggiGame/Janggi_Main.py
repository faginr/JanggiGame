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
    active_square = () #nothing selected to start
    input_clicks = [] #keep track of ticks
    row = -1
    col = -1
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
                    row = 1
                elif row > row_translation[2][0] and row < row_translation[2][1]:
                    row = 2
                elif row > row_translation[3][0] and row < row_translation[3][1]:
                    row = 3
                elif row > row_translation[4][0] and row < row_translation[4][1]:
                    row = 4
                elif row > row_translation[5][0] and row < row_translation[5][1]:
                    row = 5
                elif row > row_translation[6][0] and row < row_translation[6][1]:
                    row = 6
                elif row > row_translation[7][0] and row < row_translation[7][1]:
                    row = 7
                elif row > row_translation[8][0] and row < row_translation[8][1]:
                    row = 8
                elif row > row_translation[9][0] and row < row_translation[9][1]:
                    row = 9
                elif row > row_translation[10][0] and row < row_translation[10][1]:
                    row = 10

                if col > col_translation[1][0] and col < col_translation[1][1]:
                    col = 1
                elif col > col_translation[2][0] and col < col_translation[2][1]:
                    col = 2
                elif col > col_translation[3][0] and col < col_translation[3][1]:
                    col = 3
                elif col > col_translation[4][0] and col < col_translation[4][1]:
                    col = 4
                elif col > col_translation[5][0] and col < col_translation[5][1]:
                    col = 5
                elif col > col_translation[6][0] and col < col_translation[6][1]:
                    col = 6
                elif col > col_translation[7][0] and col < col_translation[7][1]:
                    col = 7
                elif col > col_translation[8][0] and col < col_translation[8][1]:
                    col = 8
                elif col > col_translation[9][0] and col < col_translation[9][1]:
                    col = 9

                if active_square == (row, col): #user clicked same square twice
                #     #pass your turn
                     game_state.make_move(input_clicks[0], input_clicks[0])
                     active_square = () #deselect
                     input_clicks = [] #clear click log
                elif row > 0 and row < 11 and col > 0 and col < 10:
                     active_square = (row, col)
                     input_clicks.append(active_square) #append both first and second clicks
                else:
                     active_square = ()  # deselect
                     input_clicks = []  # clear click log
                #was this the second click?
                if len(input_clicks) == 2:  # second click
                     game_state.make_move(input_clicks[0], input_clicks[1])
                     active_square = ()
                     input_clicks = []


        drawGame(screen, game_state, row, col)
        clock.tick(MAX_FPS)
        pygame.display.flip()


def drawGame(screen, game_state, row, col):
    '''draw board and pieces'''
    game_state = Janggi_Engine.JanggiGameState()
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



# row_translation = {
#         "1_lower": 75,
#         "1_upper": 125,
#         "2_lower": 150,
#         "2_upper": 175,
#         "3_lower": 225,
#         "3_upper": 250,
#         "4_lower": 275,
#         "4_upper": 325,
#         "5_lower": 350,
#         "5_upper": 400,
#         "6_lower": 425,
#         "6_upper": 475,
#         "7_lower": 500,
#         "7_upper": 550,
#         "8_lower": 600,
#         "8_upper": 650,
#         "9_lower": 675,
#         "9_upper": 725,
#         "10_lower": 750,
#         "10_upper": 800,
#     }
#     col_translation = {
#         "1_lower": 75,
#         "1_upper": 125,
#         "2_lower": 150,
#         "2_upper": 175,
#         "3_lower": 225,
#         "3_upper": 250,
#         "4_lower": 275,
#         "4_upper": 325,
#         "5_lower": 350,
#         "5_upper": 400,
#         "6_lower": 425,
#         "6_upper": 475,
#         "7_lower": 500,
#         "7_upper": 550,
#         "8_lower": 600,
#         "8_upper": 650,
#         "9_lower": 675,
#         "9_upper": 725
#     }