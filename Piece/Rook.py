from Piece.Piece import *
from Position import *
class Rook(Piece):
    def changePosition(self, destination_position, player, game):
        possibles_moves = self.getPossiblesMoves(player)
        print(possibles_moves)
        if destination_position.isIn(possibles_moves):
            self.verified_positions(destination_position, player, game)

    def getPossiblesMoves(self, player):
        all_possibles_moves = list()
        movables = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        for movable in movables:
            i=1
            while True:
                try:
                    pos = Position(self.positions.x + (movable[0]) * i, self.positions.y + (movable[1] * i))
                    print(pos)
                    if player.hasPiece(pos):
                        break
                    elif player.opponent.hasPiece(pos):
                        all_possibles_moves.append(pos)
                        break
                    all_possibles_moves.append(pos)
                    i = i+1
                except Exception:
                    break

        return all_possibles_moves