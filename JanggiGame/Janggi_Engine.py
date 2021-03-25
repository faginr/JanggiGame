'''
Game engine contains data and rules
'''


from JanggiGame import Janggi_Pieces

class JanggiGameState():

    def __init__(self):
        '''
        initializes data members:
        self._board - outer list contains entire board
                            inner lists contain rows
                                spaces contain pieces or nothing
        self._win_state - intializes to 'UNFINISHED'
        '''
        self._win_state = 'UNFINISHED'
        self._turn = 'r'
        self._board = [
            # Board
            [
                # Col Labels
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'
            ],
            [
                # Row 1
                Janggi_Pieces.Chariot('Ct', 'r', 1, 1, JanggiGameState),
                Janggi_Pieces.Elephant('El', 'r', 1, 2, JanggiGameState),
                Janggi_Pieces.Horse('Hs', 'r', 1, 3, JanggiGameState),
                Janggi_Pieces.Guard('Gd', 'r', 1, 4, JanggiGameState),
                None,
                Janggi_Pieces.Guard('Gd', 'r', 1, 6, JanggiGameState),
                Janggi_Pieces.Elephant('El', 'r', 1, 7, JanggiGameState),
                Janggi_Pieces.Horse('Hs', 'r', 1, 8, JanggiGameState),
                Janggi_Pieces.Chariot('Ct', 'r', 1, 9, JanggiGameState)
            ],
            [
                # Row 2
                None,
                None,
                None,
                None,
                Janggi_Pieces.General('Gn', 'r', 2, 5, JanggiGameState),
                None,
                None,
                None,
                None

            ],
            [
                None,
                Janggi_Pieces.Cannon('Cn', 'r', 3, 2, JanggiGameState),
                None,
                None,
                None,
                None,
                None,
                Janggi_Pieces.Cannon('Cn', 'r', 3, 8, JanggiGameState),
                None
                # Row 3

            ],
            [
                # Row 4
                Janggi_Pieces.Soldier('Sd', 'r', 4, 1, JanggiGameState),
                None,
                Janggi_Pieces.Soldier('Sd', 'r', 4, 3, JanggiGameState),
                None,
                Janggi_Pieces.Soldier('Sd', 'r', 4, 5, JanggiGameState),
                None,
                Janggi_Pieces.Soldier('Sd', 'r', 4, 7, JanggiGameState),
                None,
                Janggi_Pieces.Soldier('Sd', 'r', 4, 9, JanggiGameState),
            ],
            [
                # Row 5
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None
            ],
            [
                # Row 6
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None
            ],
            [
                # Row 7
                Janggi_Pieces.Soldier('Sd', 'b', 7, 1, JanggiGameState),
                None,
                Janggi_Pieces.Soldier('Sd', 'b', 7, 3, JanggiGameState),
                None,
                Janggi_Pieces.Soldier('Sd', 'b', 7, 5, JanggiGameState),
                None,
                Janggi_Pieces.Soldier('Sd', 'b', 7, 7, JanggiGameState),
                None,
                Janggi_Pieces.Soldier('Sd', 'b', 7, 9, JanggiGameState),
            ],
            [
                # Row 8
                None,
                Janggi_Pieces.Cannon('Cn', 'b', 8, 2, JanggiGameState),
                None,
                None,
                None,
                None,
                None,
                Janggi_Pieces.Cannon('Cn', 'b', 8, 8, JanggiGameState),
                None
            ],
            [
                # Row 9
                None,
                None,
                None,
                None,
                Janggi_Pieces.General('Gn', 'b', 9, 5, JanggiGameState),
                None,
                None,
                None,
                None
            ],
            [
                # Row 10
                Janggi_Pieces.Chariot('Ct', 'b', 10, 1, JanggiGameState),
                Janggi_Pieces.Elephant('El', 'b', 10, 2, JanggiGameState),
                Janggi_Pieces.Horse('Hs', 'b', 10, 3, JanggiGameState),
                Janggi_Pieces.Guard('Gd', 'b', 10, 4, JanggiGameState),
                None,
                Janggi_Pieces.Guard('Gd', 'b', 10, 6, JanggiGameState),
                Janggi_Pieces.Elephant('El', 'b', 10, 7, JanggiGameState),
                Janggi_Pieces.Horse('Hs', 'b', 10, 8, JanggiGameState),
                Janggi_Pieces.Chariot('Ct', 'b', 10, 9, JanggiGameState)
            ]
        ]

    def get_board(self):
        '''return current board state'''
        return self._board


    def perform_move(self, source, destination):
        '''Make a move on the board. sets source to destination, and clears source '''
        board = self.get_board()
        board[destination[0]][destination[1]] = board[source[0]][source[1]]
        board[source[0]][source[1]] = None

    def get_game_state(self):
        '''returns current win state (self._win_state)'''
        return self._win_state

    def set_game_state(self, team):
        '''sets the win state to a given team as a winner'''
        if team == 'red':
            self._win_state = 'RED_WON'
        if team == 'blue':
            self._win_state = 'BLUE_WON'

    def save_temp_state(self, temp_move_from, temp_move_to):
        '''saves move_from and move_to data'''
        self._temp_move_from = temp_move_from
        self._temp_move_to = temp_move_to

    def reload_temp_state(self, source, destination):
        '''reloads move_from and move_to data to board.'''
        board = self.get_board()
        board[source[0]][source[1]] = self._temp_move_from
        board[destination[0]][destination[1]] = self._temp_move_to


    def get_turn(self):
        '''gets current turn team'''
        return self._turn

    def set_turn(self):
        '''sets turn to opposite team color'''

        if self._turn == 'red':
            self._turn = 'blue'
        else:
            self._turn = 'red'

    def get_piece(self, row, col):
        '''returns piece occupying row/col'''
        return self._board[row][col]

    def get_coordinates(self, location):
        '''takes a board placement and translates and returns it as row/col numbers'''

        # make a dictionary keying column letters to grid values
        column_conversion=  {'a':0,
                   'b':1,
                   'c':2,
                   'd':3,
                   'e':4,
                   'f':5,
                   'g':6,
                   'h':7,
                   'i':8,
                  }

        # create new coordinates
        coords = []
        # first append row
        coords.append(location[1:])
        # second append column
        coords.append(location[:1])
        # check if valid
        if coords[1] not in column_conversion:
            return False
        # add column
        coords[1] = column_conversion[coords[1]]
        # verify and add row
        if int(coords[0]) == False:
            return False
        coords[0] = int(coords[0])
        # return [row, column] in integer form
        return coords

    def generate_check_moves(self, team):
        '''
        Takes a team. Gets current state of board,
        and generates all possible moves for team, and returns them as a list
        '''
        # get board
        board = self.get_board()
        all_moves = []
        for row in range(1,11,1):
            for col in range(0,9,1):
                # For each space on the board, determine if space is empty
                if board[row][col] is not None:
                    # If not, determine which team it is
                    if board[row][col].get_team() == team:
                        # If its the correct team, get the piece, name and location
                        piece = board[row][col]
                        piece_name = piece.get_name()
                        source = [row,col]
                        if piece_name == 'Ct':
                            # determine possible moves for chariot
                            destinations = piece.chariot_possible_destinations(source)
                            for space in destinations:
                                if piece.is_blocked(team, source, space, board) != True:
                                    all_moves.append(space)
                        elif piece_name == 'El':
                            # determine possible moves for elephant
                            destinations = piece.elephant_possible_destinations(source)
                            for space in destinations:
                                if piece.is_blocked(team, source, space, board) != True:
                                    all_moves.append(space)
                        elif piece_name == 'Hs':
                            # determine possible moves for horse
                            destinations = piece.horse_possible_destinations(source)
                            for space in destinations:
                                if piece.is_blocked(team, source, space, board) != True:
                                    all_moves.append(space)
                        elif piece_name == 'Cn':
                            # determine possible moves for cannon
                            destinations = piece.cannon_possible_destinations(source)
                            for space in destinations:
                                target = space
                                if board[target[0]][target[1]] != None:
                                    if board[target[0]][target[1]].get_name() != 'Cn':
                                        if piece.is_blocked(team, source, space, board) != True:
                                            all_moves.append(space)
                        elif piece_name == 'Sd':
                            # determine possible moves for soldier
                            destinations = piece.soldier_possible_destinations(team, source)
                            for space in destinations:
                                if piece.is_blocked(team, space, board) != True:
                                    all_moves.append(space)

        return all_moves

    def is_in_check(self, team):
        '''Takes team, checks if team is in check.
        Returns True if yes, otherwise False'''

        # Find all possible moves for other teams pieces
        # build list of all possible moves for opposing team
        if team == 'blue':
            opposing_team = 'red'
        else:
            opposing_team = 'blue'
        board = self.get_board()
        for row in range(1,11,1):
            for col in range(0,9,1):
                # For each space on the board, determine if space is empty
                if board[row][col] is not None:
                    # Find team's general
                    if board[row][col].get_team() == team:
                        if board[row][col].get_name() == 'Gn':
                            current_general_space = [row,col]

        # Generate opposing team's possible move list
        opposing_team_moves = self.generate_check_moves(opposing_team)
        if current_general_space in opposing_team_moves:
            # If at least one piece can capture general, team is in check
            return True
        else:
            return False


    def is_in_checkmate(self, team):
        '''Takes a team and checks if team's general can escape check.
        If general is in checkmate, returns True.
        Otherwise returns False'''

        # get current board state
        board = self.get_board()
        current_team_pieces = []
        # find all of team in questions pieces
        for row in range(1,11,1):
            for col in range(0,9,1):
                if board[row][col] is not None:
                    if board[row][col].get_team() == team:
                        current_piece = board[row][col]
                        current_team_pieces.append([row,col,current_piece])

        # For each piece, get all valid moves
        for piece in range(0,len(current_team_pieces),1):
            # Get piece information
            test_piece = current_team_pieces[piece][2]
            source = [current_team_pieces[piece][0],current_team_pieces[piece][1]]
            piece_destinations = self.get_possible_moves(test_piece, team, source)
            valid_piece_destinations = []
            # Test which moves are valid
            for move in piece_destinations:
                valid_move = self.test_valid_move(test_piece, team, source, move, piece_destinations)
                if valid_move == True:
                    valid_piece_destinations.append(move)

            # Try each valid move
            for move in valid_piece_destinations:
                # save state
                self.save_temp_state(board[source[0]][source[1]], board[move[0]][move[1]])
                # determine if a piece is captured
                self.perform_capture(move)
                # move piece
                self.perform_move(source, move)
                # Test if team is still in check
                if self.is_in_check(team) == False:
                    # If not reload and return false
                    self.reload_temp_state(source, move)
                    return False
                # otherwise reload and go to next move
                self.reload_temp_state(source, move)
        # If all moves still result in check, then it is checkmate
        return True


    def valid_location(self, location):
        '''takes a location and returns true if its within the bounds of the board'''

        # check if row is in board's bounds
        if location[0] < 1 or location[0] > 10:
            # print('invalid row location')
            return False

        # check if col is in board's bounds
        elif location[1] < 0 or location[1] > 8:
            # print('invalid col location')
            return False
        return True
        # print(self._board[location[0]][location[1]].get_name())


    def get_possible_moves(self, piece, team, source):
        '''switch type method to parse piece type and return appropriate possible move set'''

        # get piece name
        piece_name = piece.get_name()
        # get current board state
        board = self.get_board()

        # route to correct piece type move generation
        if piece_name == 'Ct':
            # determine possible moves for chariot
            all_moves = piece.chariot_possible_destinations(source)
            return all_moves
        elif piece_name == 'El':
            # determine possible moves for elephant
            all_moves = piece.elephant_possible_destinations(source)
            return all_moves
        elif piece_name == 'Hs':
            # determine possible moves for horse
            all_moves = piece.horse_possible_destinations(source)
            return all_moves
        elif piece_name == 'Gd':
            # determine possible moves for guard
            all_moves = piece.guard_possible_destinations(team, source)
            return all_moves
        elif piece_name == 'Gn':
            # determine possible moves for general
            all_moves = piece.general_possible_destinations(team, source)
            return all_moves
        elif piece_name == 'Cn':
            # generate possible moves for cannon
            all_moves = piece.cannon_possible_destinations(source)
            return all_moves
        elif piece_name == 'Sd':
            # generate possible moves for soldier
            all_moves = piece.soldier_possible_destinations(team, source)
            return all_moves
        else:
            # if this space doesn't have a valid piece type, return False
            return False

    def test_valid_move(self, piece, team, source, destination, all_moves):
        '''Given piece type, team color, source, destinationo, and possible moves,
        determines whether destination is a valid move and if piece is blocked.
        '''

        # get piece name
        piece_name = piece.get_name()
        # get current board state
        board = self.get_board()

        # route to correct piece type move generation
        if piece_name == 'Ct' or piece_name == 'El' or piece_name == 'Hs':
            if destination not in all_moves:
                return False
            # if the move is a valid one, is it blocked by a teammate?
            if piece.is_blocked(team, source, destination, board) != True:
                return True
            else:
                return False
        elif piece_name == 'Gd' or piece_name == 'Gn' or piece_name == 'Sd':
            if destination not in all_moves:
                return False
            # if the move is a valid one, is it blocked by a teammate?
            if piece.is_blocked(team, destination, board) != True:
                return True
            else:
                return False
        elif piece_name == 'Cn':
            # Cannot target another cannon
            target = board[destination[0]][destination[1]]
            if target != None:
                if target.get_name() == 'Cn':
                    return False
            if destination not in all_moves:
                return False
            # if the move is a valid one, is it blocked by a teammate?
            if piece.is_blocked(team, source, destination, board) != True:
                return True
            else:
                return False


    def perform_capture(self, destination):
        '''takes a destination, and removes occupying piece if any is present'''

        # get contents of destination
        destination_piece = self._board[destination[0]][destination[1]]

        # if it has a piece remove it
        if destination_piece != None:
            self._board[destination[0]][destination[1]] = None


    def make_move(self, move_from, move_to):
        '''
        Takes move_from and move_to column letter, row number
        Determines if game is over
        Validates source square and destination square
        Validates team turn
        Attempts to move, and processes captures.
        Updates turn
        Checks for check and checkmate
        Updates game win state
        '''

        # check win_state, proceed if unfinished
        if self.get_game_state() != 'UNFINISHED':
            return self.get_game_state()

        # translate move_from and move_to into row and col numbers
        source = self.get_coordinates(move_from)
        destination = self.get_coordinates(move_to)

        # validate conversion
        if source == False:
            return False

        if destination == False:
            return False

        # validate source and destination. If either is off the board, return invalid move
        if self.valid_location(source) == False:
            return False
        if self.valid_location(destination) == False:
            return False

        # check whose turn it is
        current_turn = self.get_turn()

        # get current board state
        board = self.get_board()

        # check if move from is the correct player
        if board[source[0]][source[1]] == None:
            return False
        elif current_turn != board[source[0]][source[1]].get_team():
            # if not return False
            return False

        # save move_from and move_to data
        self.save_temp_state(board[source[0]][source[1]], board[destination[0]][destination[1]])

        # is the player passing?
        if source != destination:

            # if no, get current piece at source(move_from)
            current_piece = board[source[0]][source[1]]

            # generate current piece's possible moves
            all_moves = self.get_possible_moves(current_piece, current_turn, source)
            if all_moves == False:
                return False
            # test if destination is a valid move
            test_move = self.test_valid_move(current_piece, current_turn, source, destination, all_moves)

            # If so, proceed to make move
            if test_move == True:

                # determine if a piece is captured
                self.perform_capture(destination)

                # move piece
                self.perform_move(source, destination)

            # otherwise, invalid move, return False
            else:
                return False


        # test for check
        # Set current team and opposing team
        current_team = current_turn
        if current_team == 'blue':
            opposing_team = 'red'
        else:
            opposing_team = 'blue'

        # did current player put themselves in check?
        if self.is_in_check(current_team):
            # If so, move is invalid. Reload move and return false.
            self.reload_temp_state(source, destination)
            return False

        # did current player put opposing player in check?
        if self.is_in_check(opposing_team):
            # If so, check for checkmate
            if self.is_in_checkmate(opposing_team) == True:
                # If in checkmate, game is over, set win state
                self.set_game_state(current_team)

        # update turn to next player
        self.set_turn()

        # Helper prints out move_from and move_to
        print("Attempting: ", move_from, "->", move_to)

        return True


    def print_board(self):
        '''prints out visual representation of board and current pieces in their locations'''

        # Get board state
        board = self.get_board()

        # print col header
        print("     ",board[0][0], "",
              "  ", board[0][1], "",
              "  ", board[0][2], "",
              "  ", board[0][3], "",
              "  ", board[0][4], "",
              "  ", board[0][5], "",
              "  ", board[0][6], "",
              "  ", board[0][7], "",
              "  ", board[0][8], "",
              )

        # create a new row
        for row in range(1,11,1):
            if row < 10:
                # space offset for first 9 rows
                board_output = [' |']
            else:
                # 10th row will have an extra character
                board_output = ['|']

            # for each space
            for col in range(0, 9, 1):

                # get and print team and name for each space
                if self._board[row][col] is not None:
                     space_output =  board[row][col].get_team()[:1] + board[row][col].get_name()
                     board_output.append(space_output)
                     board_output.append('|')
                # print blank for unoccupied spaces
                else:
                     space_output = "   "
                     board_output.append(space_output)
                     board_output.append('|')

            # print row
            print(row, board_output[0],
                  board_output[1],
                  board_output[2],
                  board_output[3],
                  board_output[4],
                  board_output[5],
                  board_output[6],
                  board_output[7],
                  board_output[8],
                  board_output[9],
                  board_output[10],
                  board_output[11],
                  board_output[12],
                  board_output[13],
                  board_output[14],
                  board_output[15],
                  board_output[16],
                  board_output[17],
                  board_output[18],
                  )

            # print boarders between rows
            if row == 1 or row == 8:
                print("    -----------------------\-----/-----------------------")
            elif row == 2 or row == 9:
                print("    -----------------------/-----\-----------------------")
            else:
                print("    -----------------------------------------------------")