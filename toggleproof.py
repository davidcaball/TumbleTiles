import tumbletiles as TT
from sets import Set
from getFile import getFile, parseFile
import time

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
	# Set to hold all position that have been visited
	visitedPositions = Set()
	
	# Gets the empty board from the .xml file
	boardData = parseFile("Examples/emptyboard.xml")
	board = boardData[0]

	

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

	
	for c in board.ConcreteTiles:
	 	print "concrete at ", c.x, ", ", c.y
	for p in board.Polyominoes:
	 	for tile in p.Tiles:
	 		print "tile of id ", tile.id, " at ", tile.x, ", ", tile.y

	for c in board.ConcreteTiles:
	 	for x in board.ConcreteTiles:
	 		if c != x:
	 			if c.x == x.x and c.y == x.y:
	 				print "tile ", c, " and tile ", x, " are both at ", c.x, ", ", c.y
	print "number of concrete tiles: ", len(board.ConcreteTiles)

if __name__ =="__main__":
        
    createTree("21003603")






	
	
	






