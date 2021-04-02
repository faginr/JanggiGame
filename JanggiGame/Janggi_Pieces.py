'''
Contains piece specific behaviors and attributes
'''

class Piece:
    '''
    Class defining generic game piece.
    Piece class includes:
    initial data members: game, piece_name, team, location
    methods: get_team, get_name, get_palace
    '''

    def __init__(self, piece_name, team, row, col, game):
        '''
        Initializes data members for Piece class.
        initial data members: game - Passes reference to Game class
                              piece_name - defines the name of the piece type
                              team - the team color of the piece
                              location - the location [row,col] of the piece on the board
                              palace - defines palace location on board
        '''
        self._game = game
        self._piece_name = piece_name
        self._team = team
        self._location = [row, col]
        self._palace = [
                  [1,3],[1,4],[1,5],
                  [2,3],[2,4],[2,5],
                  [3,3],[3,4],[3,5],

                  [8,3],[8,4],[8,5],
                  [9,3],[9,4],[9,5],
                  [10,3],[10,4],[10,5]
                        ]

    def get_team(self):
        '''returns the team color of the piece'''
        return self._team

    def get_name(self):
        '''returns the name of the piece'''
        return self._piece_name

    def get_palace(self):
        '''returns the palace spaces on the board'''
        return self._palace

    def get_game_state(self):
        '''returns game reference'''
        return self._game

class Soldier(Piece):
    '''
    Class defining Soldier game piece.
    Piece class includes:
    initial data members: inherits all from Piece
    methods: inherits all from Piece, soldier_possible_destinations, is_blocked
    '''

    def __init__(self, piece_name, team, row, col, game):
        '''Uses Piece characteristics. See Piece Init'''
        super().__init__(piece_name, team, row, col, game)


    def soldier_possible_destinations(self, team, source):
        '''
        Takes team and source
        determines all possible moves and returns as a list
        '''

        # get source row and col
        source_row = source[:1]
        source_col = source[1:]

        # create blank list for all possible moves
        possible_destinations = []

        # Team Red moves
        if team == 'r':

            # define all move types
            move_s = [int(source_row[0]) + 1, int(source_col[0])]
            move_w = [int(source_row[0]), int(source_col[0]) - 1]
            move_e = [int(source_row[0]), int(source_col[0]) + 1]
            move_sw = [int(source_row[0]) + 1, int(source_col[0]) - 1]
            move_se = [int(source_row[0]) + 1, int(source_col[0]) + 1]

            # add all regular moves
            # move S
            possible_destinations.append(move_s)
            # move W
            possible_destinations.append(move_w)
            # move E
            possible_destinations.append(move_e)

            #Starting in palace?
            palace = self.get_palace()
            # If in palace
            if source in palace:
                # add special moves for special palace spaces
                if source == [8,3]:
                    #move SE
                    possible_destinations.append(move_se)
                if source == [8,5]:
                    #move SW
                    possible_destinations.append(move_sw)
                if source  == [9,4]:
                    # move SE
                    possible_destinations.append(move_se)
                    # move SW
                    possible_destinations.append(move_sw)

        # Team Blue moves
        if team == 'b':

            # define all move types
            move_n = [int(source_row[0]) - 1, int(source_col[0])]
            move_w = [int(source_row[0]), int(source_col[0]) - 1]
            move_e = [int(source_row[0]), int(source_col[0]) + 1]
            move_nw = [int(source_row[0]) - 1, int(source_col[0]) - 1]
            move_ne = [int(source_row[0]) - 1, int(source_col[0]) + 1]

            # move N
            possible_destinations.append(move_n)
            # move W
            possible_destinations.append(move_w)
            # move E
            possible_destinations.append(move_e)

            #Starting in palace?
            palace = self.get_palace()
            # If in palace
            if source in palace:
                # add special moves for special palace spaces
                if source == [3,3]:
                    #move NE
                    possible_destinations.append(move_ne)
                if source == [3,5]:
                    #move SW
                    possible_destinations.append(move_nw)
                if source  == [2,4]:
                    # move SE
                    possible_destinations.append(move_ne)
                    # move SW
                    possible_destinations.append(move_nw)

        #Validate which moves are on the board
        valid_destinations = []
        game = self.get_game_state()
        for move in possible_destinations:
            if game.valid_location(game, move) == True:
                valid_destinations.append(move)

        return valid_destinations


    def is_blocked(self, current_team, destination, board):
        '''
        takes current_team, destination and board.
        determines if destination is blocked by teammate
        '''

        # Get piece occupying destination if any
        destination_piece = board[destination[0]][destination[1]]

        # If a teammate is present, return True
        if destination_piece != None:
            if destination_piece.get_team() == current_team:
                return True
        return False


class General(Piece):
    '''
    Class defining General game piece.
    Piece class includes:
    initial data members: inherits all from Piece
    methods: inherits all from Piece, genereate_possible_destinations, is_blocked
    '''

    def __init__(self, piece_name, team, row, col, game):
        '''Uses Piece characteristics. See Piece Init'''
        super().__init__(piece_name, team, row, col, game)

    def general_possible_destinations(self, team, source):
        '''
        Takes team, and source.
        determines all possible moves and returns as a list
        '''

        # get source row and col
        source_row = source[:1]
        source_col = source[1:]

        # create blank list for all possible moves
        possible_destinations = []

        # Get palace spaces
        palace = self.get_palace()

        # Team Red moves
        if team == 'r':

            # define all move types
            move_n = [int(source_row[0]) - 1, int(source_col[0])]
            move_nw = [int(source_row[0]) - 1, int(source_col[0]) - 1]
            move_ne = [int(source_row[0]) - 1, int(source_col[0]) + 1]
            move_s = [int(source_row[0]) + 1, int(source_col[0])]
            move_w = [int(source_row[0]), int(source_col[0]) - 1]
            move_e = [int(source_row[0]), int(source_col[0]) + 1]
            move_sw = [int(source_row[0]) + 1, int(source_col[0]) - 1]
            move_se = [int(source_row[0]) + 1, int(source_col[0]) + 1]

            # add all regular moves
            possible_destinations.append(move_n)
            possible_destinations.append(move_w)
            possible_destinations.append(move_s)
            possible_destinations.append(move_e)

            # add special palace moves
            if source == [1, 3]:
                possible_destinations.append(move_se)
            if source == [1, 5]:
                possible_destinations.append(move_sw)
            if source == [2, 4]:
                possible_destinations.append(move_sw)
                possible_destinations.append(move_nw)
                possible_destinations.append(move_se)
                possible_destinations.append(move_ne)
            if source == [3, 3]:
                possible_destinations.append(move_ne)
            if source == [3, 5]:
                possible_destinations.append(move_nw)

        # Team Red moves
        if team == 'b':

            # define all move types
            move_n = [int(source_row[0]) - 1, int(source_col[0])]
            move_nw = [int(source_row[0]) - 1, int(source_col[0]) - 1]
            move_ne = [int(source_row[0]) - 1, int(source_col[0]) + 1]
            move_s = [int(source_row[0]) + 1, int(source_col[0])]
            move_w = [int(source_row[0]), int(source_col[0]) - 1]
            move_e = [int(source_row[0]), int(source_col[0]) + 1]
            move_sw = [int(source_row[0]) + 1, int(source_col[0]) - 1]
            move_se = [int(source_row[0]) + 1, int(source_col[0]) + 1]

            # add all regular moves
            possible_destinations.append(move_n)
            possible_destinations.append(move_w)
            possible_destinations.append(move_s)
            possible_destinations.append(move_e)

            # add special palace moves
            if source == [8, 3]:
                possible_destinations.append(move_se)
            if source == [8, 5]:
                possible_destinations.append(move_sw)
            if source == [9, 4]:
                possible_destinations.append(move_sw)
                possible_destinations.append(move_nw)
                possible_destinations.append(move_se)
                possible_destinations.append(move_ne)
            if source == [10, 3]:
                possible_destinations.append(move_ne)
            if source == [10, 5]:
                possible_destinations.append(move_nw)

        # Validate which moves are in the palace
        valid_destinations = []
        for move in possible_destinations:
            if move in palace:
                valid_destinations.append(move)

        return valid_destinations


    def is_blocked(self, current_team, destination, board):
        '''
        takes current_team and destination.
        determines if destination is blocked by teammate
        '''

        # Get piece occupying destination if any
        destination_piece = board[destination[0]][destination[1]]

        # If a teammate is present, return True
        if destination_piece != None:
            if destination_piece.get_team() == current_team:
                return True
        return False

class Guard(Piece):
    '''
    Class defining Guard game piece.
    Piece class includes:
    initial data members: inherits all from Piece
    methods: inherits all from Piece, genereate_possible_destinations, is_blocked
    '''

    def __init__(self, piece_name, team, row, col, game):
        '''Uses Piece characteristics. See Piece Init'''
        super().__init__(piece_name, team, row, col, game)

    def guard_possible_destinations(self, team, source):
        '''
        Takes team, source and destination
        determines all possible moves and returns as a list
        '''

        # get source row and col
        source_row = source[:1]
        source_col = source[1:]

        # create blank list for all possible moves
        possible_destinations = []

        # Get palace spaces
        palace = self.get_palace()

        # Team Red moves
        if team == 'r':

            # define all move types
            move_n = [int(source_row[0]) - 1, int(source_col[0])]
            move_nw = [int(source_row[0]) - 1, int(source_col[0]) - 1]
            move_ne = [int(source_row[0]) - 1, int(source_col[0]) + 1]
            move_s = [int(source_row[0]) + 1, int(source_col[0])]
            move_w = [int(source_row[0]), int(source_col[0]) - 1]
            move_e = [int(source_row[0]), int(source_col[0]) + 1]
            move_sw = [int(source_row[0]) + 1, int(source_col[0]) - 1]
            move_se = [int(source_row[0]) + 1, int(source_col[0]) + 1]


            # add all regular moves
            possible_destinations.append(move_n)
            possible_destinations.append(move_w)
            possible_destinations.append(move_s)
            possible_destinations.append(move_e)

            # add special palace moves
            if source == [1, 3]:
                possible_destinations.append(move_se)
            if source == [1, 5]:
                possible_destinations.append(move_sw)
            if source == [2, 4]:
                possible_destinations.append(move_sw)
                possible_destinations.append(move_nw)
                possible_destinations.append(move_se)
                possible_destinations.append(move_ne)
            if source == [3, 3]:
                possible_destinations.append(move_ne)
            if source == [3, 5]:
                possible_destinations.append(move_nw)

        # Team Red moves
        if team == 'b':

            # define all move types
            move_n = [int(source_row[0]) - 1, int(source_col[0])]
            move_s = [int(source_row[0]) + 1, int(source_col[0])]
            move_w = [int(source_row[0]), int(source_col[0]) - 1]
            move_e = [int(source_row[0]), int(source_col[0]) + 1]
            move_nw = [int(source_row[0]) - 1, int(source_col[0]) - 1]
            move_ne = [int(source_row[0]) - 1, int(source_col[0]) + 1]
            move_sw = [int(source_row[0]) + 1, int(source_col[0]) - 1]
            move_se = [int(source_row[0]) + 1, int(source_col[0]) + 1]

            # add all regular moves
            possible_destinations.append(move_n)
            possible_destinations.append(move_w)
            possible_destinations.append(move_s)
            possible_destinations.append(move_e)

            # add special palace moves
            if source == [8, 3]:
                possible_destinations.append(move_se)
            if source == [8, 5]:
                possible_destinations.append(move_sw)
            if source == [9, 4]:
                possible_destinations.append(move_sw)
                possible_destinations.append(move_nw)
                possible_destinations.append(move_se)
                possible_destinations.append(move_ne)
            if source == [10, 3]:
                possible_destinations.append(move_ne)
            if source == [10, 5]:
                possible_destinations.append(move_nw)

        # Validate which moves are in the palace
        valid_destinations = []
        for move in possible_destinations:
            if move in palace:
                valid_destinations.append(move)

        return valid_destinations


    def is_blocked(self, current_team, destination, board):
        '''
        takes current_team and destination.
        determines if destination is blocked by teammate
        '''

        # Get piece occupying destination if any
        destination_piece = board[destination[0]][destination[1]]

        # If a teammate is present, return True
        if destination_piece != None:
            if destination_piece.get_team() == current_team:
                return True
        return False

class Chariot(Piece):
    '''
    Class defining Chariot game piece.
    Piece class includes:
    initial data members: inherits all from Piece
    methods: inherits all from Piece, genereate_possible_destinations, is_blocked
    '''

    def __init__(self, piece_name, team, row, col, game):
        '''Uses Piece characteristics. See Piece Init'''
        super().__init__(piece_name, team, row, col, game)

    def chariot_possible_destinations(self, source):
        '''
        Takes team, source and destination
        determines all possible moves and returns as a list
        '''

        # get source row and col
        source_row = source[:1]
        source_col = source[1:]

        # create blank list for all possible moves
        possible_destinations = []

        # Get palace spaces
        palace = self.get_palace()

        # palace moves
        move_nw = [int(source_row[0]) - 1, int(source_col[0]) - 1]
        double_move_nw = [int(source_row[0]) - 2, int(source_col[0]) - 2]
        move_ne = [int(source_row[0]) - 1, int(source_col[0]) + 1]
        double_move_ne = [int(source_row[0]) - 2, int(source_col[0]) + 2]
        move_sw = [int(source_row[0]) + 1, int(source_col[0]) - 1]
        double_move_sw = [int(source_row[0]) + 2, int(source_col[0]) - 2]
        move_se = [int(source_row[0]) + 1, int(source_col[0]) + 1]
        double_move_se = [int(source_row[0]) + 2, int(source_col[0]) + 2]

        # varible will keep track of all possible distances to move
        distance = 1

        # Maximum possible travel is 9 spaces
        while distance < 10:

            # regular moves
            move_n = [int(source_row[0]) - distance, int(source_col[0])]
            move_s = [int(source_row[0]) + distance, int(source_col[0])]
            move_w = [int(source_row[0]), int(source_col[0]) - distance]
            move_e = [int(source_row[0]), int(source_col[0]) + distance]

            possible_destinations.append(move_n)
            possible_destinations.append(move_s)
            possible_destinations.append(move_w)
            possible_destinations.append(move_e)
            distance += 1

        # If in palace
        if source in palace:
            # add special moves for special palace spaces
            # Red palace
            if source == [1, 3]:
                possible_destinations.append(move_se)
                possible_destinations.append(double_move_se)
            if source == [1, 5]:
                possible_destinations.append(move_sw)
                possible_destinations.append(double_move_sw)
            if source == [2, 4]:
                possible_destinations.append(move_sw)
                possible_destinations.append(move_nw)
                possible_destinations.append(move_ne)
                possible_destinations.append(move_se)
            if source == [3, 3]:
                possible_destinations.append(move_ne)
                possible_destinations.append(double_move_ne)
            if source == [3, 5]:
                possible_destinations.append(move_nw)
                possible_destinations.append(double_move_nw)

            # Blue palace
            if source == [8, 3]:
                possible_destinations.append(move_se)
                possible_destinations.append(double_move_se)
            if source == [8, 5]:
                possible_destinations.append(move_sw)
                possible_destinations.append(double_move_sw)
            if source == [9, 4]:
                possible_destinations.append(move_sw)
                possible_destinations.append(move_nw)
                possible_destinations.append(move_ne)
                possible_destinations.append(move_se)
            if source == [10, 3]:
                possible_destinations.append(move_ne)
                possible_destinations.append(double_move_ne)
            if source == [10, 5]:
                possible_destinations.append(move_nw)
                possible_destinations.append(double_move_nw)

        # Validate which moves are on the board
        valid_destinations = []
        game = self.get_game_state()
        for move in possible_destinations:
            if game.valid_location(game, move) == True:
                valid_destinations.append(move)

        return valid_destinations


    def is_blocked(self, current_team, source, destination, board):
        '''
        takes current_team and destination.
        determines if destination is blocked by teammate
        '''

        # Get palace
        palace = self.get_palace()

        direction = None

        # Get direction of travel
        if source[0] > destination[0]:  #n
            direction = 'n'
            # Determine if move starts in palace
            if source in palace:
                if source[1] > destination[1]:  # w
                    direction = 'nw'
                elif source[1] < destination[1]:  # e
                    direction = 'ne'
                else:
                    direction = 'n'
        elif source[0] < destination[0]:    #s
            direction = 's'
            # Determine if move starts in palace
            if source in palace:
                if source[1] > destination[1]:  # w
                    direction = 'sw'
                elif source[1] < destination[1]:  # e
                    direction = 'se'
        elif source[1] > destination[1]:    #w
            direction = 'w'
        elif source[1] < destination[1]:    #e
            direction = 'e'

        # Test path moving north
        if direction == 'n':
            # For each space between source and destination exclusive
            distance = source[0] - destination[0] - 1
            path = 1
            # check if any space is occupied
            while distance > 0:
                next_space_piece = board[source[0] - path][source[1]]
                if next_space_piece != None:
                    return True
                distance -= 1
                path += 1

        # Test path moving south
        if direction == 's':
            # For each space between source and destination exclusive
            distance = destination[0] - source[0] - 1
            path = 1
            # check if any space is occupied
            while distance > 0:
                next_space_piece = board[source[0] + path][source[1]]
                if next_space_piece != None:
                    return True
                distance -= 1
                path += 1

        # Test path moving east
        if direction == 'e':
            # For each space between source and destination exclusive
            distance = destination[1] - source[1] - 1
            path = 1
            # check if any space is occupied
            while distance > 0:
                next_space_piece = board[source[0]][source[1] + path]
                if next_space_piece != None:
                    return True
                distance -= 1
                path += 1

        # Test path moving west
        if direction == 'w':
            # For each space between source and destination exclusive
            distance = source[1] - destination[1] - 1
            path = 1
            # check if any space is occupied
            while distance > 0:
                next_space_piece = board[source[0]][source[1] - path]
                if next_space_piece != None:
                    return True
                distance -= 1
                path += 1

        # Test path moving northwest
        if direction == 'nw':
            # For each space between source and destination exclusive
            distance = source[0] - destination[0] - 1
            path = 1
            # check if any space is occupied
            while distance > 0:
                next_space_piece = board[source[0] - path][source[1] - path]
                if next_space_piece != None:
                    return True
                distance -= 1
                path += 1

        # Test path moving northeast
        if direction == 'ne':
            # For each space between source and destination exclusive
            distance = source[0] - destination[0] - 1
            path = 1
            # check if any space is occupied
            while distance > 0:
                next_space_piece = board[source[0] - path][source[1] + path]
                if next_space_piece != None:
                    return True
                distance -= 1
                path += 1

        # Test path moving southwest
        if direction == 'sw':
            # For each space between source and destination exclusive
            distance = destination[0] - source[0] - 1
            path = 1
            # check if any space is occupied
            while distance > 0:
                next_space_piece = board[source[0] + path][source[1]-path]
                if next_space_piece != None:
                    return True
                distance -= 1
                path += 1

        # Test path moving southeast
        if direction == 'se':
            # For each space between source and destination exclusive
            distance = destination[0] - source[0] - 1
            path = 1
            # check if any space is occupied
            while distance > 0:
                next_space_piece = board[source[0] + path][source[1] + path]
                if next_space_piece != None:
                    return True
                distance -= 1
                path += 1

        # Get piece occupying destination if any
        destination_piece = board[destination[0]][destination[1]]

        # If a teammate is present, return True
        if destination_piece != None:
            if destination_piece.get_team() == current_team:
                return True
        return False

class Horse(Piece):
    '''
    Class defining Horse game piece.
    Piece class includes:
    initial data members: inherits all from Piece
    methods: inherits all from Piece, genereate_possible_destinations, is_blocked
    '''

    def __init__(self, piece_type, team, row, col, game):
        '''Uses Piece characteristics. See Piece Init'''
        super().__init__(piece_type, team, row, col, game)

    def horse_possible_destinations(self, source):
        '''
        Takes team, source and destination
        determines all possible moves and returns as a list
        '''

        # get source row and col
        source_row = source[:1]
        source_col = source[1:]

        # create blank list for all possible moves
        possible_destinations = []

        # define move types
        move_nne = [int(source_row[0]) - 2, int(source_col[0]) + 1]
        move_nnw = [int(source_row[0]) - 2, int(source_col[0]) - 1]
        move_wwn = [int(source_row[0]) - 1, int(source_col[0]) - 2]
        move_wws = [int(source_row[0]) + 1, int(source_col[0]) - 2]
        move_ssw = [int(source_row[0]) + 2, int(source_col[0]) - 1]
        move_sse = [int(source_row[0]) + 2, int(source_col[0]) + 1]
        move_ees = [int(source_row[0]) + 1, int(source_col[0]) + 2]
        move_een = [int(source_row[0]) - 1, int(source_col[0]) + 2]

        possible_destinations.append(move_nne)
        possible_destinations.append(move_nnw)
        possible_destinations.append(move_wwn)
        possible_destinations.append(move_wws)
        possible_destinations.append(move_ssw)
        possible_destinations.append(move_sse)
        possible_destinations.append(move_ees)
        possible_destinations.append(move_een)

        # Validate which moves are on the board
        valid_destinations = []
        game = self.get_game_state()
        for move in possible_destinations:
            if game.valid_location(game, move) == True:
                valid_destinations.append(move)

        return valid_destinations


    def is_blocked(self, current_team, source, destination, board):
        '''
        takes current_team and destination.
        determines if destination is blocked by teammate
        '''

        # get direction of travel
        direction = None

        # Get direction of travel
        if destination[0] == source[0] - 2: # moving north first
            next_space_piece = board[source[0] - 1][source[1]]
            if next_space_piece != None:
                return True
        if destination[0] == source[0] + 2: # moving south first
            next_space_piece = board[source[0] + 1][source[1]]
            if next_space_piece != None:
                return True
        if destination[1] == source[1] - 2: # moving west first
            next_space_piece = board[source[0]][source[1] - 1]
            if next_space_piece != None:
                return True
        if destination[1] == source[1] + 2: # moving east first
            next_space_piece = board[source[0]][source[1] + 1]
            if next_space_piece != None:
                return True

        # Get piece occupying destination if any
        destination_piece = board[destination[0]][destination[1]]

        # If a teammate is present, return True
        if destination_piece != None:
            if destination_piece.get_team() == current_team:
                return True
        return False



class Elephant(Piece):
    '''
    Class defining Elephant game piece.
    Piece class includes:
    initial data members: inherits all from Piece
    methods: inherits all from Piece, genereate_possible_destinations, is_blocked
    '''

    def __init__(self, piece_type, team, row, col, game):
        '''Uses Piece characteristics. See Piece Init'''
        super().__init__(piece_type, team, row, col, game)

    def elephant_possible_destinations(self, source):
        '''
        Takes team, source and destination
        determines all possible moves and returns as a list
        '''
        # get source row and col
        source_row = source[:1]
        source_col = source[1:]

        # create blank list for all possible moves
        possible_destinations = []

        # define move types
        move_nnene = [int(source_row[0]) - 3, int(source_col[0]) + 2]
        move_nnwnw = [int(source_row[0]) - 3, int(source_col[0]) - 2]
        move_wwnwn = [int(source_row[0]) - 2, int(source_col[0]) - 3]
        move_wwsws = [int(source_row[0]) + 2, int(source_col[0]) - 3]
        move_sswsw = [int(source_row[0]) + 3, int(source_col[0]) - 2]
        move_ssese = [int(source_row[0]) + 3, int(source_col[0]) + 2]
        move_eeses = [int(source_row[0]) + 2, int(source_col[0]) + 3]
        move_eenen = [int(source_row[0]) - 2, int(source_col[0]) + 3]

        possible_destinations.append(move_nnene)
        possible_destinations.append(move_nnwnw)
        possible_destinations.append(move_wwnwn)
        possible_destinations.append(move_wwsws)
        possible_destinations.append(move_sswsw)
        possible_destinations.append(move_ssese)
        possible_destinations.append(move_eeses)
        possible_destinations.append(move_eenen)

        # Validate which moves are on the board
        valid_destinations = []
        game = self.get_game_state()
        for move in possible_destinations:
            if game.valid_location(game, move) == True:
                valid_destinations.append(move)

        return valid_destinations


    def is_blocked(self, current_team, source, destination, board):
        '''
        takes current_team and destination.
        determines if destination is blocked by teammate
        '''

        # get direction of travel
        direction = None

        # Get direction of travel
        if destination[0] == source[0] - 3:  # moving north first
            next_space_piece = board[source[0] - 1][source[1]]
            if next_space_piece != None:
                return True
            if destination[1] == source[1] - 2:  #moving west
                next_space_piece = board[source[0] - 2][source[1] - 1]
                if next_space_piece != None:
                    return True
            if destination[1] == source[1] + 2: #moving east
                next_space_piece = board[source[0] - 2][source[1] + 1]
                if next_space_piece != None:
                    return True

        if destination[0] == source[0] + 3:  # moving south first
            next_space_piece = board[source[0] + 1][source[1]]
            if next_space_piece != None:
                return True
            if destination[1] == source[1] - 2:  # moving west
                next_space_piece = board[source[0] + 2][source[1] - 1]
                if next_space_piece != None:
                    return True
            if destination[1] == source[1] + 2:  # moving east
                next_space_piece = board[source[0] + 2][source[1] + 1]
                if next_space_piece != None:
                    return True

        if destination[1] == source[1] - 3:  # moving west first
            next_space_piece = board[source[0]][source[1] - 1]
            if next_space_piece != None:
                return True
            if destination[0] == source[0] - 2:  #moving north
                next_space_piece = board[source[0] - 1][source[1] - 2]
                if next_space_piece != None:
                    return True
            if destination[0] == source[0] + 2: #moving south
                next_space_piece = board[source[0] + 1][source[1] - 2]
                if next_space_piece != None:
                    return True

        if destination[1] == source[1] + 3:  # moving east first
            next_space_piece = board[source[0]][source[1] + 1]
            if next_space_piece != None:
                return True
            if destination[0] == source[0] - 2:  #moving north
                next_space_piece = board[source[0] - 1][source[1] + 2]
                if next_space_piece != None:
                    return True
            if destination[0] == source[0] + 2: #moving south
                next_space_piece = board[source[0] + 1][source[1] + 2]
                if next_space_piece != None:
                    return True

        # Get piece occupying destination if any
        destination_piece = board[destination[0]][destination[1]]

        # If a teammate is present, return True
        if destination_piece != None:
            if destination_piece.get_team() == current_team:
                return True
        return False

class Cannon(Piece):
    '''
    Class defining Cannon game piece.
    Piece class includes:
    initial data members: inherits all from Piece
    methods: inherits all from Piece, genereate_possible_destinations, is_blocked
    '''

    def __init__(self, piece_type, team, row, col, game):
        '''Uses Piece characteristics. See Piece Init'''
        super().__init__(piece_type, team, row, col, game)

    def cannon_possible_destinations(self, source):
        '''
        Takes team, source and destination
        determines all possible moves and returns as a list
        '''

        # get source row and col
        source_row = source[:1]
        source_col = source[1:]

        # create blank list for all possible moves
        possible_destinations = []

        # Get palace spaces
        palace = self.get_palace()

        # palace moves
        double_move_nw = [int(source_row[0]) - 2, int(source_col[0]) - 2]
        double_move_ne = [int(source_row[0]) - 2, int(source_col[0]) + 2]
        double_move_sw = [int(source_row[0]) + 2, int(source_col[0]) - 2]
        double_move_se = [int(source_row[0]) + 2, int(source_col[0]) + 2]

        # varible will keep track of all possible distances to move. must move at least 2.
        distance = 2

        # Maximum possible travel is 9 spaces
        while distance < 10:
            # regular moves
            move_n = [int(source_row[0]) - distance, int(source_col[0])]
            move_s = [int(source_row[0]) + distance, int(source_col[0])]
            move_w = [int(source_row[0]), int(source_col[0]) - distance]
            move_e = [int(source_row[0]), int(source_col[0]) + distance]

            possible_destinations.append(move_n)
            possible_destinations.append(move_s)
            possible_destinations.append(move_w)
            possible_destinations.append(move_e)
            distance += 1

        # If in palace
        if source in palace:
            # add special moves for special palace spaces
            # Red palace
            if source == [1, 3]:
                possible_destinations.append(double_move_se)
            if source == [1, 5]:
                possible_destinations.append(double_move_sw)
            if source == [3, 3]:
                possible_destinations.append(double_move_ne)
            if source == [3, 5]:
                possible_destinations.append(double_move_nw)

            # Blue palace
            if source == [8, 3]:
                possible_destinations.append(double_move_se)
            if source == [8, 5]:
                possible_destinations.append(double_move_sw)
            if source == [10, 3]:
                possible_destinations.append(double_move_ne)
            if source == [10, 5]:
                possible_destinations.append(double_move_nw)

        # Validate which moves are on the board
        valid_destinations = []
        game = self.get_game_state()
        for move in possible_destinations:
            if game.valid_location(game, move) == True:
                valid_destinations.append(move)

        return valid_destinations


    def is_blocked(self, current_team, source, destination, board):
        '''
        takes current_team and destination.
        determines if destination is blocked by teammate
        '''

        # Get palace
        palace = self.get_palace()

        direction = None

        # Get direction of travel
        if source[0] > destination[0]:  # n
            direction = 'n'
            # Determine if move starts in palace
            if source in palace:
                if source[1] > destination[1]:  # w
                    direction = 'nw'
                elif source[1] < destination[1]:  # e
                    direction = 'ne'
                else:
                    direction = 'n'
        elif source[0] < destination[0]:  # s
            direction = 's'
            # Determine if move starts in palace
            if source in palace:
                if source[1] > destination[1]:  # w
                    direction = 'sw'
                elif source[1] < destination[1]:  # e
                    direction = 'se'
        elif source[1] > destination[1]:  # w
            direction = 'w'
        elif source[1] < destination[1]:  # e
            direction = 'e'

        # Get piece occupying destination if any
        destination_piece = board[destination[0]][destination[1]]

        # Keep track of jump
        has_jumped = False

        # Get reference to game
        game = self.get_game_state()

        # Test path moving north
        if direction == 'n':
            # For each space between source and destination exclusive
            distance = source[0] - destination[0] - 1
            path = 1
            # check if any space is occupied
            while distance > 0:
                next_space_piece = board[source[0] - path][source[1]]
                if next_space_piece != None:
                    if has_jumped == True:
                        return True
                    if next_space_piece.get_name() == 'Cn':
                        return True
                    has_jumped = True
                distance -= 1
                path += 1

        # Test path moving south
        if direction == 's':
            # For each space between source and destination exclusive
            distance = destination[0] - source[0] - 1
            path = 1
            # check if any space is occupied
            while distance > 0:
                next_space_piece = board[source[0] + path][source[1]]
                if next_space_piece != None:
                    if has_jumped == True:
                        return True
                    if next_space_piece.get_name() == 'Cn':
                        return True
                    has_jumped = True
                distance -= 1
                path += 1

        # Test path moving east
        if direction == 'e':
            # For each space between source and destination exclusive
            distance = destination[1] - source[1] - 1
            path = 1
            # check if any space is occupied
            while distance > 0:
                next_space_piece = board[source[0]][source[1] + path]
                if next_space_piece != None:
                    if has_jumped == True:
                        return True
                    if next_space_piece.get_name() == 'Cn':
                        return True
                    has_jumped = True
                distance -= 1
                path += 1

        # Test path moving west
        if direction == 'w':
            # For each space between source and destination exclusive
            distance = source[1] - destination[1] - 1
            path = 1
            # check if any space is occupied
            while distance > 0:
                next_space_piece = board[source[0]][source[1] - path]
                if next_space_piece != None:
                    if has_jumped == True:
                        return True
                    if next_space_piece.get_name() == 'Cn':
                        return True
                    has_jumped = True
                distance -= 1
                path += 1

        # Test path moving northwest
        if direction == 'nw':
            # For each space between source and destination exclusive
            distance = source[0] - destination[0] - 1
            path = 1
            # check if any space is occupied
            while distance > 0:
                next_space_piece = board[source[0] - path][source[1] - path]
                if next_space_piece != None:
                    if has_jumped == True:
                        return True
                    if next_space_piece.get_name() == 'Cn':
                        return True
                    has_jumped = True
                distance -= 1
                path += 1

        # Test path moving northeast
        if direction == 'ne':
            # For each space between source and destination exclusive
            distance = source[0] - destination[0] - 1
            path = 1
            # check if any space is occupied
            while distance > 0:
                next_space_piece = board[source[0] - path][source[1] + path]
                if next_space_piece != None:
                    if has_jumped == True:
                        return True
                    if next_space_piece.get_name() == 'Cn':
                        return True
                    has_jumped = True
                distance -= 1
                path += 1

        # Test path moving southwest
        if direction == 'sw':
            # For each space between source and destination exclusive
            distance = destination[0] - source[0] - 1
            path = 1
            # check if any space is occupied
            while distance > 0:
                next_space_piece = board[source[0] + path][source[1] - path]
                if next_space_piece != None:
                    if has_jumped == True:
                        return True
                    if next_space_piece.get_name() == 'Cn':
                        return True
                    has_jumped = True
                distance -= 1
                path += 1

        # Test path moving southeast
        if direction == 'se':
            # For each space between source and destination exclusive
            distance = destination[0] - source[0] - 1
            path = 1
            # check if any space is occupied
            while distance > 0:
                next_space_piece = board[source[0] + path][source[1] + path]
                if next_space_piece != None:
                    if has_jumped == True:
                        return True
                    if next_space_piece.get_name() == 'Cn':
                        return True
                    has_jumped = True
                distance -= 1
                path += 1

        # Get piece occupying destination if any
        destination_piece = board[destination[0]][destination[1]]

        # If a teammate is present, return True
        if destination_piece != None:
            if destination_piece.get_name() == 'Cn':
                return True
            if destination_piece.get_team() == current_team:
                return True
        if has_jumped == False:
            return True
        return False
