from Player import *
from Position import *
class Game():
    def __init__(self):
        self.moves = []
        self.startGame()

    def startGame(self):

        # Initialisation des joueurs et attribution à la classe
        self.black_player = Player('black')
        self.white_player = Player('white')
        self.black_player.opponent = self.white_player
        self.white_player.opponent = self.black_player


    def move(self, src, dst):
        # Conversion des notation algébrique en numérique
        xSrc, ySrc = toNumberCoord(src)
        xDst, yDst = toNumberCoord(dst)

        # Conversion de la valeur numérique en objet position
        source = Position(xSrc, ySrc)
        destination = Position(xDst, yDst)

        # Verification qui ont le trait
        if len(self.moves) % 2 == 0:
            current_player = self.white_player
        else:
            current_player = self.black_player

        # Mouvement pour le joueur qui aura le trait
        current_player.movePiece(source, destination, self)
    
    def smallCastling(self):

        if len(self.moves) % 2 == 0:
            self.white_player.smallCastling()
        else:
            self.black_player.smallCastling()
        self.saveCastling("O-O")
            
    def bigCastling(self):
        if len(self.moves) % 2 == 0:
            self.white_player.bigCastling()
            
        else:
            self.black_player.bigCastling()
        self.saveCastling("O-O-O")
    
    def canContinue(self, sourcePosition, destinationPosition):
        self.moves.append((sourcePosition, destinationPosition))
    
    def saveCastling(self, castling):
        self.moves.append(castling)

    def clearBoard(self):
        self.white_player.pieces = []
        self.black_player.pieces = []

    def turnOf(self):
        if len(self.moves) % 2 == 0:
            return "white"
        else:
            return "black"