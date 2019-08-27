from Piece import *
from Piece.Pawn import *
from Piece.Rook import *
from Piece.Knight import *
from Piece.Bishop import *
from Piece.Queen import *
from Piece.King import *
from ChessRulesExceptions import PositionException
from Position import *
class Player(object):
    def __init__(self, color):
        self.color = color
        self.new_game()
    
    def movePiece(self, sourcePosition, destinationPosition, game):

        piece = self.findPiece(sourcePosition)
        print(self.color +" "+ str(destinationPosition))
        piece.changePosition(destinationPosition, self, game)


    def findPiece(self,positions):
        for piece in self.pieces:
            if piece.positions.equals(positions.x, positions.y):
                return piece
        raise PositionException("No matching piece in x="+str(positions.x)+",y="+str(positions.y))

    def hasPiece(self, positions):
        for piece in self.pieces:
            if piece.positions.equals(positions.x,positions.y):
                return True
        return False


    def new_game(self):
        pieces = list()

        # Pawn initialisation
        for i in range(1,8):
            if self.color == "black":
                pieces.append(Pawn(i, 7))
            if self.color == "white":
                pieces.append(Pawn(i, 2))
                
        # Rook initialisation
        if self.color == "black":
            pieces.append(Rook(1, 8))
            pieces.append(Rook(8, 8))
        if self.color == "white":
            pieces.append(Rook(1, 1))
            pieces.append(Rook(8, 1))
            
        # Knight initialisation
        if self.color == "black":
            pieces.append(Knight(2, 8))
            pieces.append(Knight(7, 8))
        if self.color == "white":
            pieces.append(Knight(2, 1))
            pieces.append(Knight(7, 1))
        
        # Bishop initialisation
        if self.color == "black":
            pieces.append(Bishop(3, 8))
            pieces.append(Bishop(6, 8))
        if self.color == "white":
            pieces.append(Bishop(3, 1))
            pieces.append(Bishop(6, 1))

        # Queen initialisation
        if self.color == "black":
            pieces.append(Queen(4, 8))
        if self.color == "white":
            pieces.append(Queen(4, 1))

        # King initialisation
        if self.color == "black":
            pieces.append(King(5, 8))
        if self.color == "white":
            pieces.append(King(5, 1))

        self.pieces = pieces

    def remove_passable(self):
        for piece in self.pieces:
            if piece.typeOf() == "Pawn":
                piece.passable=False