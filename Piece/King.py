from Piece.Piece import *
from Position import *
class King(Piece):
    def changePosition(self, destination_position, player, game):
        possibles_moves = self.getPossiblesMoves(player)
        # print(possibles_moves)
        if destination_position.isIn(possibles_moves):
            self.verified_positions(destination_position, player, game)
        else:
            raise PositionException("impossible king's move")

    def getDangerousPositions(self, player):
        dangerous_positions = list()
        for piece in player.opponent.pieces:
            if piece.typeOf() != "Pawn" and piece.typeOf()!="King":
                dangerous_positions = dangerous_positions + piece.getPossiblesMoves(player.opponent)
            if piece.typeOf() == "Pawn":
                dangerous_positions += piece.getCapturablePositions(player.opponent)
        return dangerous_positions

    def getCapabilities(self, player):
        king_capabilites = list()
        movables = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
        
        for movable in movables:
            try:
                pos = Position(self.positions.x + (movable[0]) , self.positions.y + (movable[1]))
                if player.hasPiece(pos):
                    continue
                elif player.opponent.hasPiece(pos):
                    king_capabilites.append(pos)
                    continue
                king_capabilites.append(pos)
            except Exception:
                continue
        return king_capabilites


    def getPossiblesMoves(self, player):
        possibles_moves = list()

        king_capabilites = self.getCapabilities(player)
        dangerous_positions = self.getDangerousPositions(player)
        king_opponent = player.opponent.getKing()
        king_opponent_capabilites = king_opponent.getCapabilities(player.opponent)
        king_opponent_dangerous_positions = king_opponent.getDangerousPositions(player.opponent)

        for king_opponent_capability in king_opponent_capabilites:
            if king_opponent_capability.isIn(king_opponent_dangerous_positions) and king_opponent_capability.isIn(king_capabilites):
                possibles_moves.append(king_opponent_capability)
            elif not king_opponent_capability.isIn(king_opponent_dangerous_positions) and king_opponent_capability.isIn(king_capabilites) :
                dangerous_positions.append(king_opponent_capability)



        for move in king_capabilites:
            if not move.isIn(dangerous_positions) and not move.isIn(possibles_moves):
                possibles_moves.append(move)
        print(possibles_moves)
        return possibles_moves