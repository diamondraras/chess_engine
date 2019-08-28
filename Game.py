from Player import *
from Position import *
class Game():
    def __init__(self):
        self.moves = []
        self.startGame()

    def startGame(self):
        self.black_player = Player('black')
        self.white_player = Player('white')
        self.black_player.opponent = self.white_player
        self.white_player.opponent = self.black_player
        self.check = False
        self.checkmate = False
        self.draws = False

    def move(self, src, dst):
        xSrc, ySrc = toNumberCoord(src)
        xDst, yDst = toNumberCoord(dst)

        source = Position(xSrc, ySrc)
        destination = Position(xDst, yDst)
        if len(self.moves) % 2==0:
            self.white_player.movePiece(source, destination, self)
        else:
            self.black_player.movePiece(source, destination, self)
    
    def canContinue(self, sourcePosition, destinationPosition):
        self.moves.append((sourcePosition, destinationPosition))

    def clearBoard(self):
        self.white_player.pieces = []
        self.black_player.pieces = []