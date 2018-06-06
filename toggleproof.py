import tumbletiles as TT
from sets import Set
from getFile import getFile, parseFile
import time

#										"[bluex][bluey][redx][redy]"
# Structure for starting and end coordinates is "21003603"
visitedPositions = Set()
startingPositions = Set()
stuckPositions = Set()
redEscapedPosition = Set()
solvedPositions = Set()
solvedNodes = []
board = None


class Tree(object):
	def __init__(self, coordinates):
		self.coordinates = coordinates
		self.up = None
		self.down = None
		self.right = None
		self.left = None
		self.stuck = False
		self.redundant = False
		self.solved = False
		self.parent = None


# Fills all the sets with data from the text files
def initializeSets():
	startFile = open()

# Takes a board and returns the coordinates of the red and blue tile in the correct format
def getCoordinateString()
	global board

	bluePoly = board.Polyominoes[1]
	blueX = str(bluePoly.Tiles[0].x)  
	blueY = str(bluePoly.Tiles[0].y) 

	redPoly = board.Polyominoes[0]

	redX = str(redPoly.Tiles[0].x)
	redY = str(redPoly.Tiles[0].y)

	if len(blueX) == 1:
		blueX = "0" + blueX
	if len(blueY) == 1:
		blueY = "0" + blueY
	if len(redX) == 1:
		redX = "0" + redX
	if len(redY) == 1:
		redY = "0" + redY
	coordString = blueX + blueY + redX + redY
	print(coordString)

	return coordString





def revertBoardToStart(startingPosition):
	blueX = int(startingPosition[:2])
	blueY = int(startingPosition[2:4])

	redX = int(startingPosition[4:6])
	redY = int(startingPosition[6:8])

	bluePoly = board.Polyominoes[1]
	bluePoly.Tiles[0].x = blueX
	bluePoly.Tiles[0].y = blueY

	bluePoly.Tiles[1].x = blueX + 1
	bluePoly.Tiles[1].y = blueY

	bluePoly.Tiles[2].x = blueX
	bluePoly.Tiles[2].y = blueY + 1

	bluePoly.Tiles[3].x = blueX + 1
	bluePoly.Tiles[3].y = blueY + 1

	redPoly = board.Polyominoes[0]

	redPoly.Tiles[0].x = redX
	redPoly.Tiles[0].y = redY

def recurseTree(root, startingPosition):


	newNode = Tree(startingPosition)
	newNode.parent = root

	if startingPosition is in visitedPositions:
		newNode.redundant = True
	else:
		visitedPositions.add(startingPosition)

	if startingPosition is in stuckPositions:
		newNode.stuck = True

	if startingPosition is in solvedPositions:
		newNode.solve = True
		solvedNodes.append(newNode)
	
	if !newNode.stuck and !newNode.redundant:

		board.tumble("N")
		newNode.up = recurseTree(newNode, getCoordinateString())

		revertBoardToStart()
		board.tumble("S")
		newNode.down = recurseTree(newNode, getCoordinateString())

		revertBoardToStart()
		board.tumble("E")
		newNode.right = recurseTree(newNode, getCoordinateString())

		revertBoardToStart()
		board.tumble("W")
		newNode.left = recurseTree(newNode, getCoordinateString())

		return newNode

	



def createTree(startingPosition):
	global board
	# Set to hold all position that have been visited
	visitedPositions = Set()
	root = Tree(startingPosition)
	
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

	recurseTree(root, startingPosition)

	
	# for c in board.ConcreteTiles:
	#  	print "concrete at ", c.x, ", ", c.y
	# for p in board.Polyominoes:
	#  	for tile in p.Tiles:
	#  		print "tile of id ", tile.id, " at ", tile.x, ", ", tile.y

	# for c in board.ConcreteTiles:
	#  	for x in board.ConcreteTiles:
	#  		if c != x:
	#  			if c.x == x.x and c.y == x.y:
	#  				print "tile ", c, " and tile ", x, " are both at ", c.x, ", ", c.y
	# print "number of concrete tiles: ", len(board.ConcreteTiles)




if __name__ =="__main__":
        
    createTree("21003603")






	
	
	






