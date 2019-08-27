from Piece.Piece import *
from Position import *
from ChessRulesExceptions import PositionException

class Pawn(Piece):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.moved = False

    def changePosition(self, destination_position, player, game):
        possibles_moves = self.getPossiblesMoves(player)
        print(possibles_moves)
        # print( Position(xDst, yDst) in possibles_moves)
        if destination_position.isIn(possibles_moves):
            self.moved = True
            self.verified_positions(destination_position, game)
        else:
            raise PositionException("impossible pawn's move")

    def getPossiblesMoves(self, player):
        Pmoves = list()
        
        if player.color == "white":
            direction = 1
        else:
            direction = -1
        
        # Normal move
        try:
            normal_move = Position(self.positions.x, self.positions.y +(direction *1))
            if not player.opponent.hasPiece(normal_move) and not player.hasPiece(normal_move):
                Pmoves.append(normal_move)
        except Exception:
            pass
        
        # Normal First move
        try:
            first_move = Position(self.positions.x, self.positions.y +(direction * 2))
            if not player.opponent.hasPiece(first_move) and not self.moved and not player.hasPiece(normal_move):
                Pmoves.append(first_move)
                # self.passable = True
        except Exception:
            pass
            
        # Capture left move
        try:
            left_capture_move = Position(self.positions.x - 1, self.positions.y + (direction * 1))
            if player.opponent.hasPiece(left_capture_move):
                Pmoves.append(left_capture_move)
        except Exception:
            pass
        
        # Capture right move
        try:
            right_capture_move = Position(self.positions.x + 1, self.positions.y + (direction * 1))
            if player.opponent.hasPiece(right_capture_move):
                Pmoves.append(right_capture_move)
        except Exception:
            pass
            
        
        # En passant Left
        try:
            left_en_passant = Position(self.positions.x - 1, self.positions.y)
            if player.opponent.hasPiece(left_en_passant) and player.opponent.findPiece(left_en_passant).passable:
                Pmoves.append(left_en_passant)
        except expression as identifier:
            pass
            
        # En passant Right
        try:
            right_en_passant = Position(self.positions.x + 1, self.positions.y)
            if player.opponent.hasPiece(right_en_passant) and player.opponent.findPiece(right_en_passant).passable:
                Pmoves.append(right_en_passant)
        except expression as identifier:
            pass

        return Pmoves