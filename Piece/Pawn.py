from Piece.Queen import *
from Piece.Piece import *
from Position import *
from ChessRulesExceptions import PositionException

class Pawn(Piece):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.moved = False
        self.passable = False

    def checkPromotion(self, player):
        if player.color == "black":
            y = 1
        elif player.color == "white":
            y = 8
        if self.positions.y == y:
            print('promotion')
            player.pieces[player.getPieceIndex(self.positions)] = Queen(self.positions.x, y)

    def changePosition(self, destination_position,player, game):
        possibles_moves = self.getPossiblesMoves(player)
        if destination_position.isIn(possibles_moves):
            self.checkPassable(destination_position)
            self.moved = True
            self.canContinue(destination_position, player, game)
            self.checkPromotion(player)
        else:
            raise PositionException("impossible pawn's move")
    
    def checkPassable(self, destination_position):
        if abs(self.positions.y - destination_position.y) == 2:
            self.passable = True
            
    def getCapturablePositions(self, player):
        direction = self.getDirection(player)
        capturable_positions = list()
        # Capture left move
        try:
            left_capture_move = Position(self.positions.x - 1, self.positions.y + (direction * 1))
            if player.opponent.hasPiece(left_capture_move):
                capturable_positions.append(left_capture_move)
        except Exception:
            pass
        # Capture right move
        try:
            right_capture_move = Position(self.positions.x + 1, self.positions.y + (direction * 1))
            if player.opponent.hasPiece(right_capture_move):
                capturable_positions.append(right_capture_move)
        except Exception:
            pass
        return capturable_positions
    def getDirection(self, player):
        if player.color == "white":
            direction = 1
        else:
            direction = -1
        return direction

    def getPossiblesMoves(self, player):
        Pmoves = list()
        
        direction = self.getDirection(player)
        
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
            
        # Capturable positions
        capturable_positions = self.getCapturablePositions(player)
        if len(capturable_positions):
            Pmoves= Pmoves +capturable_positions
        
        
        # En passant Left
        try:
            left_en_passant_opponent = Position(self.positions.x - 1, self.positions.y)
            left_en_passant_destination = Position(self.positions.x - 1, self.positions.y + (direction))
            
            if player.opponent.hasPiece(left_en_passant_opponent) and player.opponent.findPiece(left_en_passant_opponent).passable:
                Pmoves.append(left_en_passant_destination)
        except Exception:
            pass
        
        # En passant Right
        try:
            right_en_passant_opponent = Position(self.positions.x + 1, self.positions.y)
            right_en_passant_destination = Position(self.positions.x + 1, self.positions.y + (direction))
            if player.opponent.hasPiece(right_en_passant_opponent) and player.opponent.findPiece(right_en_passant_opponent).passable:
                Pmoves.append(right_en_passant_destination)
        except Exception:
            pass
            
        return Pmoves

    def __repr__(self):
        return self.typeOf()+" "+str(self.positions)+" "+str(self.passable)+"\n"