from Position import *
class Piece():
    def __init__(self, x, y):
        self.positions = Position(x, y)
        
    def changePosition (self, positions, player, game):
        raise NotImplementedError

    def getPossiblesMoves (self, x,y):
        raise NotImplementedError

    def verified_positions(self, destination_position, game):
        self.positions = destination_position
        game.canContinue(self.positions, destination_position)
        print("ok")