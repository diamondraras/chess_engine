from Piece import *
from Piece.Pawn import *
from Piece.Rook import *
from Piece.Knight import *
from Piece.Bishop import *
from Piece.Queen import *
from Piece.King import *
from ChessRulesExceptions import PositionException
from ChessRulesExceptions import CheckException
from Position import *
from copy import *
class Player(object):
    def __init__(self, color):
        self.color = color
        self.new_game()
        self.checked = False
        self.checkmated = False
        self.draws = False
    
    def movePiece(self, sourcePosition, destinationPosition, game):
        piece = self.findPiece(sourcePosition)
        if not self.checked:
            piece.changePosition(destinationPosition, self, game)
        else:
            acceptableAvoidingCheck = self.acceptable(sourcePosition, destinationPosition)
            if self.checked and acceptableAvoidingCheck:
                piece.changePosition(destinationPosition, self, game)
            else:
                raise CheckException("Check positions must be prevented !")

    def acceptable(self, sourcePosition, destinationPosition):
        tempPlayer = copy(self)
        all_pieces = tempPlayer.pieces
        piece_to_move = tempPlayer.findPiece(sourcePosition)
        index_of_piece = all_pieces.index(piece_to_move)
        piece_to_move.positions = destinationPosition
        tempPlayer.pieces[index_of_piece] = piece_to_move
        tempPlayer.check()
        piece_to_move.positions = sourcePosition
        tempPlayer.pieces[index_of_piece] = piece_to_move
        return tempPlayer.checked == False

    def getKing(self):
        for piece in self.pieces:
            if piece.typeOf() == "King":
                return piece

    def findPiece(self,positions):
        for piece in self.pieces:
            if piece.positions.equals(positions):
                return piece
        raise PositionException(self.color+" : No matching piece in x="+str(positions.x)+",y="+str(positions.y))

    def hasPiece(self, positions):
        for piece in self.pieces:
            if piece.positions.equals(positions):
                return True
        return False

    def new_game(self):
        pieces = list()

        # Pawn initialisation
        for i in range(1,9):
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
                piece.passable = False

    def remove_piece(self, positions):
       for i, piece in enumerate(self.pieces):
            if piece.positions.equals(positions):
                del self.pieces[i]

    def check(self):
        self.checked = False
        king = self.getKing()
        king_dangerous_positions = king.getDangerousPositions(self)
        # print(king_dangerous_positions)
        king_in_danger = king.positions.isIn(king_dangerous_positions)
        # king_capabilities = king.getCapabilities(self)

        if king_in_danger:
            self.checked = True
            
        # mate = False
        # for king_capability in king_capabilities:
        #     mate = True
        #     if king_capability.isIn(king_dangerous_positions) and king_in_danger:
        #         pass
        #     else:
        #         mate = False
        #         break

        # if mate:
        #     self.checkmated = True
            
