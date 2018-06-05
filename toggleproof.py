import tumbletiles as TT
from sets import Set

#										"[bluex][bluey][redx][redy]"
# Structure for starting and end coordinates is "21003603"

startingPositions = Set()
stuckPositions = Set()
redEscapedPosition = Set()
solvedPositions = Set()


class Tree(object):
	def __init__(self):
		self.up = None
		self.down = None
		self.right = None
		self.left = None
		self.stuck = False
		self.redundant = False


def createTree(startingPosition):
	visitedPositions = Set()
	board = TT.Board(45,45)

	blueGlues = ["N","N","N","N"]
	redGlues = ["S","S","S","S"]

	#use the starting position to position the initial tiles
	blueX = int(startingPosition[:2])
	blueY = int(startingPosition[2:4])

	redX = int(startingPosition[4:6])
	redY = int(startingPosition[6:8])

	# Create the polyomino objects
	bluePoly = TT.Polyomino(1, blueX, blueY, blueGlues, "#0000ff")
	redPoly = TT.Polyomino(0, redX, redY, redGlues, "#ff0000")

	# Add the rest of the tiles to the blue square
	bluePoly.Tiles.append(TT.Tile(bluePoly, 1, blueX + 1, blueY, blueGlues, "#0000ff", False))
	bluePoly.Tiles.append(TT.Tile(bluePoly, 1, blueX, blueY + 1, blueGlues, "#0000ff", False))
	bluePoly.Tiles.append(TT.Tile(bluePoly, 1, blueX + 1, blueY + 1, blueGlues, "#0000ff", False))

	board.Add(redPoly)
	board.Add(bluePoly)

	# for p in board.Polyominoes:
	# 	for tile in p.Tiles:
	# 		print "tile of id ", tile.id, " at ", tile.x, ", ", tile.y

if __name__ =="__main__":
        
    createTree("21003603")





	
	
	






