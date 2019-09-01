from ChessRulesExceptions import PositionException
from copy import *


class Position():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def equals(self,positions):
        if self.x==positions.x and self.y==positions.y:
            return True
        else:
            return False

    def isDefended(self, player):
        temp_player = copy(player)
        all_pieces = temp_player.pieces
        piece_to_remove = temp_player.findPiece(self)
        index_of_piece = all_pieces.index(piece_to_remove)
        temp_piece = all_pieces[index_of_piece]
        del temp_player.pieces[index_of_piece]
        moves_without_piece = list()
        for piece in temp_player.pieces:
            moves_without_piece = moves_without_piece + piece.getPossiblesMoves(temp_player)
        temp_player.pieces.append(temp_piece)
        if self.isIn(moves_without_piece):
            return True
        else:
            return False

    def __setattr__(self, attr_name, attr_val):
        if attr_name == "x" or attr_name == "y":
            if attr_val < 9 and attr_val > 0:
                object.__setattr__(self, attr_name, attr_val)
            else:
                raise PositionException("Positions must in chessboard")
    
    def __repr__(self):
        return "x="+str(self.x)+" "+ "y="+str(self.y)

    def isIn(self, possibles_moves):
        for move in possibles_moves:
            if self.equals(move):
                return True
        return False
    
def toNumberCoord(alphabetical):
    aOrd = 97
    hOrd = 104

    xOrd = ord(alphabetical[0].lower())
    y = int(alphabetical[1])

    if xOrd <= hOrd and xOrd >= aOrd and y>=1 and y<=8:
        x = xOrd - 96
    else:
        raise PositionException("Positions must in chessboard")

    return x, y
