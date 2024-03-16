# Store all info about a current state of a chess game.
# Determine the valid moves at the current states

import numpy as np


class GameState():

    def __init__(self) :
        self.board  = np.array(
            [
                ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
                ['bP','bP','bP', 'bP','bP','bP', 'bP','bP'],
                ['--', '--', '--','--', '--', '--','--', '--'],
                ['--', '--', '--','--', '--', '--','--', '--'],
                ['--', '--', '--','--', '--', '--','--', '--'],
                ['--', '--', '--','--', '--', '--','--', '--'],
                ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
                ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]

            ]
        )
        self.white_to_move = True
        self.en_passant = False
        self.log = ["0000"]
        self.log_file_rank_notation = []

        self.history = [np.array(self.board[:])]

    def make_move(self, move) :
        if self.is_valid(move) and not self.en_passant:
            self.board[move.start_row, move.start_col] = '--'
            self.board[move.end_row, move.end_col] = move.piece_moved
            self.log.append(move.get_notation()[0])
            self.log_file_rank_notation.append(move.get_notation()[1])
            # print(self.move_log)
            self.white_to_move = not self.white_to_move
            # # after every move add the actual board
            self.history.append(np.array(self.board))
            print(self.log[-1])


        elif self.is_valid and self.en_passant :
            self.board[move.start_row, move.start_col] = '--'
            self.board[int(self.log[-1][3]), int(self.log[-1][2])] = '--'
            self.board[move.end_row, move.end_col] = move.piece_moved
            self.en_passant = False
            self.log.append(move.get_notation()[0])
            self.log_file_rank_notation.append(move.get_notation()[1])
            self.white_to_move = not self.white_to_move
            self.history.append(np.array(self.board))




    def is_valid(self, move) :
        #First click not on empty square and don't capture own piece
        if move.piece_moved != '--' and (move.piece_moved[0] != move.piece_captured[0]) \
            and ((move.piece_moved[0]=='w' and self.white_to_move) or (move.piece_moved[0]=='b' and not self.white_to_move)):
#--------------------------------------------------------------------------------
        # control Pawn moves
            if "P" in move.piece_moved :
                # en-passant
                if (abs(int(self.log[-1][1]) - int(self.log[-1][3])) == 2) and\
                    (move.end_col == int(self.log[-1][2])) and abs(move.end_row - int(self.log[-1][1])) == 1:
                    self.en_passant = True
                    # print(int(self.log[-1][3]))
                    # print(int(self.log[-1][1], int(self.log[-1][3])), '     should equal 2')
                    # print(move.end_col, int(self.log[-1][2]), "    should be equal")
                    # print(abs(move.end_row - int(self.log[-1][1])), "      Should equal 1")
                    # En Passant
                    print("En Passant")
                    return True

                # On starting square(black, white), (2 rows) (same file)
                elif (move.start_row in [1, 6]) and (abs(move.end_row - move.start_row) <= 2)\
                    and  (move.start_col == move.end_col)and (move.piece_captured == '--') :

                    return True
                # one row if not in start square
                elif (abs(move.end_row - move.start_row) == 1) and  (move.start_col == move.end_col) and (move.piece_captured == '--'):

                    return True

                # Capture
                elif move.piece_captured != '--' and abs(move.start_row - move.end_row) == 1 and abs(move.start_col - move.end_col) == 1 :

                    return True

#__________________________________________________________________________________________________________________________________


        return False



class Move() :

    rank_row = {
        "1" : 7, "2" : 6, "3" : 5, "4" : 4, "5" : 3, "6":2, "7":1, "8":0}

    row_rank = {v:k for k,v in rank_row.items()}

    file_col = {
        'a':0, 'b':1, 'c':2,'d':3, 'e':4, 'f':5, 'g':6, 'h':7
    }

    col_file = {v:k for k,v in file_col.items()}

    def __init__(self, start_sq, end_sq, board) :
        self.start_row = start_sq[0]
        self.start_col = start_sq[1]
        self.end_row = end_sq[0]
        self.end_col = end_sq[1]
        self.piece_moved = board[self.start_row, self.start_col]
        self.piece_captured = board[self.end_row, self.end_col]

    def get_notation(self) :
        file_rank = self.get_rank_file(self.start_row, self.start_col) + self.get_rank_file(self.end_row, self.end_col)

        numerci_representation = str(self.start_col) + str(self.start_row) + str(self.end_col) + str(self.end_row)

        return numerci_representation, file_rank

    def get_rank_file(self, r,c) :
        return self.col_file[c] + self.row_rank[r]
