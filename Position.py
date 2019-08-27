from ChessRulesExceptions import PositionException

class Position():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def equals(self, x, y):
        if self.x==x and self.y==y:
            return True
        else:
            return False
        
    def __setattr__(self, attr_name, attr_val):
        if attr_name == "x" or attr_name == "y":
            if attr_val < 9:
                object.__setattr__(self, attr_name, attr_val)
            else:
                raise PositionException("Positions must in chessboard")
    
    def __repr__(self):
        return "x="+str(self.x)+" "+ "y="+str(self.y)

    def isIn(self, possibles_moves):
        for move in possibles_moves:
            if self.equals(move.x, move.y):
                return True
        return False
    
def toNumberCoord(alphabetical):
    aOrd = 97
    hOrd = 104

    xOrd = ord(alphabetical[0].lower())
    y = int(alphabetical[1])

    if xOrd <= hOrd and xOrd >= aOrd and y>=1 and y<=8:
        x = xOrd - 96
    else:
        raise PositionException("Positions must in chessboard")

    return x, y
