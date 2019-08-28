from Piece.Piece import *
from Position import *
class Knight(Piece):
    def changePosition(self, destination_position, player, game):
        possibles_moves = self.getPossiblesMoves(player)
        if destination_position.isIn(possibles_moves):
            self.verified_positions(destination_position, player, game)
        else:
            raise PositionException("impossible knight's move")
    def getPossiblesMoves(self, player):
        all_possibles_moves = list()
        movables = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        
        for movable in movables:

            try:
                pos = Position(self.positions.x + movable[0], self.positions.y + movable[1])
                if not player.hasPiece(pos):
                    all_possibles_moves.append(pos)
            except Exception:
                pass
        return all_possibles_moves