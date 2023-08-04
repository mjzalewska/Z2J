import string

from art import tprint
from classes.piece import WhitePawn, BlackPawn, WhiteKing, BlackKing
from classes.player import Player
from classes.board import Board
from Checkers.utilities.utilities import convert


class Game:
    game_state = 'initializing'
    board = None
    player_1 = None
    player_2 = None

    # TODO: add rules ?
    @classmethod
    def show_welcome_screen(cls):
        tprint('Checkers', font='tarty1')  # tarty9
        print()
        print('Welcome to the game of Python Checkers! Let\'s start!\n')

    @classmethod
    def game_over(cls):
        tprint('Game over', font='tarty1')

    @classmethod
    def show_menu(cls):
        pass

    @classmethod
    def show_rules(cls):
        pass

    @classmethod
    def choose_game_mode(cls):
        modes = ['1', '2']
        print('Please choose how you want to play: ')
        print('1 - Player vs Player')
        print('2 - Player vs Computer')
        while True:
            mode_choice = input()
            try:
                if mode_choice in modes:
                    return mode_choice
                else:
                    raise ValueError
            except ValueError:
                print('Incorrect input. Please choose 1 or 2')

    @classmethod
    def initialize(cls):
        # initialize players
        match Game.choose_game_mode():
            case '1':
                cls.player_1 = Player('human')
                cls.player_2 = Player('human')
            case '2':
                cls.player_1 = Player('human')
                cls.player_2 = Player('computer')

        # initialize game board
        cls.board = Board()

        # initialize pawns
        for num in range(1, 13):
            w_piece = WhitePawn()
            cls.player_1.pieces.append(w_piece)

            b_piece = BlackPawn()
            cls.player_2.pieces.append(b_piece)

        # assign pawns to initial positions on board
        for line in range(len(cls.board.board_fields[:3])):
            for column in range(len(cls.board.board_fields[line])):
                if cls.board.board_fields[line][column] == ' ':
                    cls.board.board_fields[line][column] = next(iter(cls.player_1.pieces))

        for line in range(len(cls.board.board_fields[4:])):
            for column in range(len(cls.board.board_fields[line])):
                if cls.board.board_fields[-line][column] == ' ':
                    cls.board.board_fields[-line][column] = next(iter(cls.player_2.pieces))

        # assign  initial field_list position to pieces
        for piece in cls.player_1.pieces:
            for line in range(len(cls.board.board_fields[:4])):
                for column in range(len(cls.board.board_fields[line])):
                    if cls.board.board_fields[line][column] == piece:
                        piece.set_initial_position(convert(index=(line, column)))

        for piece in cls.player_1.pieces:
            for line in range(len(cls.board.board_fields[5:])):
                for column in range(len(cls.board.board_fields[line])):
                    if cls.board.board_fields[line][column] == piece:
                        piece.set_initial_position(convert(index=(line, column)))

        cls.game_state = 'playing'

    @classmethod
    def scan_for_mandatory_jumps(cls, piece):
        mandatory_moves = []
        piece_coordinates = [(line, column) for line in range(len(cls.board.board_fields))
                             for column in range(len(cls.board.board_fields[line]))
                             if cls.board.board_fields[line][column] == piece]

        for coordinates in piece_coordinates:
            line, column = coordinates
            if line in range(0,len(cls.board.board_fields)-1) and column in range(0,len(cls.board.board_fields[line])-1):
            # ograniczenie pola poszukiwań do powierzchni planszy
                left_bottom_node = cls.board.board_fields[line + 1][column + 1]
                right_bottom_node = cls.board.board_fields[line + 1][column - 1]
                left_top_node = cls.board.board_fields[line-1][column - 1]
                right_top_node = cls.board.board_fields[line-1][column +1]

                if piece.rank == 'pawn':
                    if left_bottom_node and left_bottom_node in cls.player_2.pieces or\
                            right_bottom_node and right_bottom_node in cls.player_2.pieces:
                        mandatory_moves.extend([left_bottom_node, right_bottom_node])
                        print('Mandatory jump!')
                elif piece.rank == 'king':
                    if left_bottom_node and left_bottom_node in cls.player_2.pieces or \
                            right_bottom_node and right_bottom_node in cls.player_2.pieces or\
                            left_top_node and left_top_node in cls.player_2.pieces or\
                            right_top_node and right_top_node in cls.player_2.pieces:
                        mandatory_moves.extend([left_bottom_node, right_bottom_node])
                        print('Mandatory jump')
        return mandatory_moves

    @classmethod
    def get_field_no(cls, prompt):
        board_field_list = [letter + str(num) for letter in string.ascii_uppercase[:8] for num in range(1, 9)]
        while True:
            try:
                field_no = input(prompt)
                if field_no not in board_field_list:
                    raise ValueError
                else:
                    return field_no
            except ValueError:
                print('The position you provided is not on the board. Try another field')

    @classmethod
    def check_piece_owner(cls, field_no, player):
        field_line, field_col = convert(field=field_no)
        while True:
            try:
                if Board.board_fields[field_line][field_col] not in player.pieces:
                    raise ValueError
                return True
            except ValueError:
                print("Sorry, you can only move your own pawns. Try again!")

    @classmethod
    def check_vacancy(cls, field_no):
        try:
            if not Board.is_cell_vacant(field_no):
                raise ValueError
            else:
                return field_no
        except ValueError:
            print("This field is occupied. Please choose another field!")

    @classmethod
    def play_vs_human(cls):
        # 1st player
        while True:
            if cls.game_state == 'initializing':
                cls.initialize()
            else:
                print('Player 1, your turn!')
                for piece in cls.player_1.pieces:
                    if cls.scan_for_mandatory_jumps(piece):
                        print()
                        pass # propose mandatory movements to choose from (list locations of pawns to move)
                # scan for mandatory jumps
                # if mandatory jump option present - block other moves
                # after mandatory move - if another jump possible - indicate to player
                pawn_location = cls.get_field_no('Which pawn would you like to move? Please indicate position on the '
                                                 'board: ')
                if not cls.board.is_cell_vacant(pawn_location) and cls.check_piece_owner(pawn_location, cls.player_1):
                    pass
                    # check for mandatory moves - of none, ask for target cell and do checks

                target_location = cls.get_field_no('Where would you like to move your pawn? Please indicate position '
                                                   'on the board: ')

        # check if distance correct (next field)
        # if the piece can move this way (pawns only forwards, king - both ways)
        # check if empty

        # add a scan for compulsory capture
        # always check if moved to promotion line - promote if yes

        # check if fields forwards or backwards - check if included in array[row+1:] -
        # check if target empty - check if cell vacant - func done
        # then move and change position - move -done

    @classmethod
    def show_current_score(cls):
        print()
        print(">>> Current score <<<")
        print(f"    Player 1: {cls.player_1.score}")
        print(f"    Player 2: {cls.player_2.score}")
        print()

    # player 1 move
    # check if own or enemy
    # check if target empty
    # move (define possible moves)

    # player 2 move
    # repeat the above

    # capturing
    # check if next field empty
    # check if other caputres possible - if yes lock other moves, must capture

    # monitor for promotion line

    @classmethod
    def human_vs_comp(cls):
        pass

    @classmethod
    def play_game(cls):
        pass


# manual test code
Game.initialize()
Game.board.display_board()
for piece in Game.player_1.pieces:
    print(Game.scan_for_mandatory_jumps(piece=piece))
