from Position import *
class Piece():
    def __init__(self, x, y):
        self.positions = Position(x, y)
        
    def changePosition (self, positions, player, game):
        raise NotImplementedError

    def getPossiblesMoves (self, x,y):
        raise NotImplementedError

    def verified_positions(self, destination_position, player, game):
        self.positions = destination_position
        game.canContinue(self.positions, destination_position)
        player.opponent.remove_passable()
        # print(player.pieces)
    
    def typeOf(self):
        return type(self).__name__

    def __repr__(self):
        return self.typeOf()+" "+str(self.positions)+"\n"