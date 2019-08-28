from Position import *
class Piece():
    def __init__(self, x, y):
        self.positions = Position(x, y)

    def changePosition (self, positions,player, game):
        raise NotImplementedError

    def getPossiblesMoves (self, x,y):
        raise NotImplementedError

    def verified_positions(self, destination_position, player, game):
        self.positions = destination_position
        game.canContinue(self.positions, destination_position)
        player.opponent.remove_passable()
        if player.opponent.hasPiece(destination_position):
            player.opponent.remove_piece(destination_position)
    
    def typeOf(self):
        return type(self).__name__

    def __repr__(self):
        return self.typeOf() + " " + str(self.positions) + "\n"
    
    # def __setattr__(self, attr_name, attr_val):
    #     if attr_name == "positions" and self.owner.opponent.hasPiece(attr_val):
    #         self.owner.opponent.remove_piece(attr_val)
    #     object.__setattr__(self, attr_name, attr_val)