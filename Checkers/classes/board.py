from Checkers.utilities.utilities import convert


class Board:
    board_fields = [[' 1', '2', '3', '4', '5', '6', '7', '8'],
                    ['A', '\u25A0', ' ', '\u25A0', ' ', '\u25A0', ' ', '\u25A0', ' '],
                    ['B', ' ', '\u25A0', ' ', '\u25A0', ' ', '\u25A0', ' ', '\u25A0'],
                    ['C', '\u25A0', ' ', '\u25A0', ' ', '\u25A0', ' ', '\u25A0', ' '],
                    ['D', ' ', '\u25A0', ' ', '\u25A0', ' ', '\u25A0', ' ', '\u25A0'],
                    ['E', '\u25A0', ' ', '\u25A0', ' ', '\u25A0', ' ', '\u25A0', ' '],
                    ['F', ' ', '\u25A0', ' ', '\u25A0', ' ', '\u25A0', ' ', '\u25A0'],
                    ['G', '\u25A0', ' ', '\u25A0', ' ', '\u25A0', ' ', '\u25A0', ' '],
                    ['H', ' ', '\u25A0', ' ', '\u25A0', ' ', '\u25A0', ' ', '\u25A0'],
                    ]
    promotion_lines = [board_fields[1], board_fields[-1]]

    @classmethod
    def get_vacant_cells(cls):
        vacant_cells = []
        for line in range(len(cls.board_fields)):
            for column in range(len(cls.board_fields[line])):
                if cls.board_fields[line][column] == ' ':
                    vacant_cells.append((line, column))
        return vacant_cells

    @classmethod
    def is_cell_vacant(cls, cell):
        cell_line, cell_col = convert(field=cell)
        if cls.board_fields[cell_line + 1][cell_col + 1] == ' ':
            return True
        return False

    @classmethod
    def get_next_cell(cls, cell):
        return f"{chr(ord(cell[0]) + 1)}{str(int(cell[1]) + 1)}"

    @classmethod
    def get_preceding_cell(cls, cell):
        return f"{chr(ord(cell[0]) - 1)}{str(int(cell[1]) - 1)}"

    @classmethod
    def display_board(cls):
        str_matrix = []
        for line in cls.board_fields:
            str_matrix.append([str(column) for column in line])
        print(f"  {'  '.join(str_matrix[0])}")
        for line in str_matrix[1:]:
            print('  '.join(line))
