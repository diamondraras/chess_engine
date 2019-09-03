from Position import *
from ChessRulesExceptions import PositionException
class Piece():
    def __init__(self, x, y):
        self.positions = Position(x, y)

    def changePosition (self, positions,player, game):
        raise NotImplementedError

    def getPossiblesMoves (self, x,y):
        raise NotImplementedError

    def canContinue(self, destination_position, player, game):
        self.positions = destination_position
        game.canContinue(self.positions, destination_position)
        player.opponent.remove_passable()
        if player.opponent.hasPiece(destination_position):
            player.opponent.remove_piece(destination_position)
        player.opponent.check()
        player.opponent.checkmate()
        player.opponent.drawsCheck()
    def typeOf(self):
        return type(self).__name__

    def __repr__(self):
        return self.typeOf() + " " + str(self.positions) + "\n"

    