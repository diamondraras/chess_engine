from Piece.Piece import *
from Position import *
class King(Piece):
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.moved = False
        
    def changePosition(self, destination_position, player, game):
        possibles_moves = self.getPossiblesMoves(player)
        if destination_position.isIn(possibles_moves):
            self.canContinue(destination_position, player, game)
        else:
            raise PositionException("impossible king's move")

    def getDangerousPositions(self, player):
        dangerous_positions = list()
        for i,piece in enumerate(player.opponent.pieces):
            if piece.typeOf() != "Pawn" and piece.typeOf() != "King":
                dangerous_positions = dangerous_positions + piece.getPossiblesMoves(player.opponent)
            if piece.typeOf() == "Pawn":
                dangerous_positions += piece.getCapturablePositions(player.opponent)
            if piece.typeOf() == "King":
                dangerous_positions += piece.getCapabilities(player.opponent)
        
        filtered_result = list()
        for dp in dangerous_positions:
            if not dp.isIn(filtered_result):
                filtered_result.append(dp)

        return filtered_result

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

        for king_capability in king_capabilites:
            if player.opponent.hasPiece(king_capability) and king_capability.isDefended(player.opponent):
                dangerous_positions.append(king_capability)

        for move in king_capabilites:
            if not move.isIn(dangerous_positions) and not move.isIn(possibles_moves):
                possibles_moves.append(move)
        return possibles_moves
    