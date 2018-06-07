import tumbletiles as TT
from sets import Set
from getFile import getFile, parseFile
import time

#										"[bluex][bluey][redx][redy]"
# Structure for starting and end coordinates is "21003603"
visitedPositions = Set()
startingPositions = Set()
stuckPositions = Set()
redEscapedPositions = Set()
solvedPositions1 = Set()
solvedPositions2 = Set()
solvedNodes = []
redEscapedNodes = []
board = None
nodeCount = 0
root = None
solution = ""
start =  ""


stuckSetFile = "Coordinates/stuckCoordinates.txt"

startSetFile = "Coordinates/startCoordinates.txt"

redEscSetFile = "Coordinates/redEscCoordinates.txt"


class Tree(object):
	def __init__(self, coordinates):
		self.coordinates = coordinates
		self.directionFromParent = ""
		self.north = None
		self.south = None
		self.east = None
		self.west = None
		self.stuck = False
		self.redundant = False
		self.solved = False
		self.redEscaped = False
		self.parent = None


# Fills all the sets with data from the text files
def initializeSets():
	startFile = open()

# Takes a board and returns the coordinates of the red and blue tile in the correct format
def getCoordinateString():
	global board
	if len(board.Polyominoes[1].Tiles) == 4:
		bluePoly = board.Polyominoes[1]
	else:
		print "error"

	blueX = bluePoly.Tiles[0].x  
	blueY = bluePoly.Tiles[0].y

	if bluePoly.Tiles[1].x < blueX or bluePoly.Tiles[1].y < blueY:
		blueX = bluePoly.Tiles[1].x
		blueY = bluePoly.Tiles[1].y

	if bluePoly.Tiles[2].x < blueX or bluePoly.Tiles[2].y < blueY:
		blueX = bluePoly.Tiles[2].x
		blueY = bluePoly.Tiles[2].y

	if bluePoly.Tiles[3].x < blueX or bluePoly.Tiles[3].y < blueY:
		blueX = bluePoly.Tiles[3].x
		blueY = bluePoly.Tiles[3].y

	blueX = str(blueX)
	blueY = str(blueY)

	if len(board.Polyominoes[0].Tiles) == 1:
		redPoly = board.Polyominoes[0]
	else:
		print "error"

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
	# print(coordString)

	return coordString





def revertBoardToStart(startingPosition):
	blueX = int(startingPosition[:2])
	blueY = int(startingPosition[2:4])

	redX = int(startingPosition[4:6])
	redY = int(startingPosition[6:8])

	print "BlueX: ", blueX, "\nBlueY: ", blueY, "\nRedX: ", redX, "\nRedY: ", redY
	
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

	print "Current Positions\n Blue:\n1: ", bluePoly.Tiles[0].x, ", ", bluePoly.Tiles[0].y, "\n2: ", bluePoly.Tiles[1].x, ", ", bluePoly.Tiles[1].y, "\n3: ", bluePoly.Tiles[2].x, ", ", bluePoly.Tiles[2].y, "\n4: ", bluePoly.Tiles[3].x, ", ", bluePoly.Tiles[3].y 
	# time.sleep(5)
	# board.ActivateGlues()

def recurseTree(root, startingPosition, direction):
	global nodeCount
	# print(nodeCount)
	nodeCount = nodeCount + 1

	newNode = Tree(startingPosition)
	newNode.parent = root
	newNode.directionFromParent = direction

	print "CURRENT POSITION: ", getCoordinateString()

	if startingPosition in visitedPositions:
		newNode.redundant = True
	else:
		visitedPositions.add(startingPosition)

	if startingPosition in stuckPositions:
		newNode.stuck = True

	if startingPosition[:4] == solution:
		newNode.solve = True
		solvedNodes.append(newNode)

	if startingPosition[4:8] in redEscapedPositions:
		newNode.redEscaped = True
		redEscapedNodes.append(newNode)

	
	if not newNode.stuck and not newNode.redundant and not newNode.solved and not newNode.redEscaped:

		board.Tumble("N")
		newConfig = getCoordinateString()
		if not "N" == newNode.directionFromParent and newConfig not in visitedPositions:
			newNode.north = recurseTree(newNode, newConfig,"N")

		revertBoardToStart(startingPosition)

		board.Tumble("S")
		newConfig = getCoordinateString()
		if not "S" == newNode.directionFromParent and newConfig not in visitedPositions:
			newNode.north = recurseTree(newNode, newConfig,"S")

		revertBoardToStart(startingPosition)

		board.Tumble("E")
		newConfig = getCoordinateString()
		if not "E" == newNode.directionFromParent and newConfig not in visitedPositions:
			newNode.north = recurseTree(newNode, newConfig,"E")

		revertBoardToStart(startingPosition)

		board.Tumble("W")
		newConfig = getCoordinateString()
		if not "W" == newNode.directionFromParent and newConfig not in visitedPositions:
			newNode.north = recurseTree(newNode, newConfig,"W")

		return newNode

# Loads the positions for the stuck positions, solved positions, 
# and red escaped positions into their respective sets
def loadSets():
	global stuckSetFile 
	global startSetFile 
	global redEscSetFile

	stuckFile = open(stuckSetFile, "r")
	startFile = open(startSetFile, "r")
	redEscFile = open(redEscSetFile, "r")

	for l in startFile.readlines():
		startingPositions.add(l[:8])

	for l in stuckFile.readlines():
		stuckPositions.add(l[:8])

	for l in redEscFile.readlines():
		redEscapedPositions.add(l[:4])

	print "Created Sets: \nSize of starting: ", len(startingPositions), "\nSize of stuck: ", len(stuckPositions), "\nLength of redEsc: ", len(redEscapedPositions)



def printSequence(node):
	if node.directionFromParent == "START":
		return

	printSequence(node.parent)

	print node.directionFromParent, " - ", node.coordinates


def logSequence(node, file):
	if node.directionFromParent == "START":
		return

	logSequence(node.parent, file)

	file.write(node.directionFromParent)

def logData():
	file = open("Log/log.txt", "w")
	file.write(start + "\n")
	file.write("****************************\nSolutions:\n")
	for node in solvedNodes:
		file.write(start)
		logSequence(node, file)
		file.write("\n")
	file.write("****************************\n****************************\nRed Escape:\n")

	for node in redEscapedNodes:
		file.write(start)
		logSequence(node, file)
		file.write("\n")

		


def createTree(startingPosition):
	global solution
	global board
	global root
	global start
	start = startingPosition
	# Set to hold all position that have been visited

	loadSets()

	#set determines if the solution should be in the blue in the bottom and right or
	if startingPosition[:4] == "2100":
		solution = "1838"
	elif startingPosition[:4] == "0020":
		solution = "3817"
	elif startingPosition[:4] == "3817":
		solution = "0020"
	elif startingPosition[:4] == "1838":
		solution = "2100"

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

	recurseTree(root, startingPosition, "START")

	print "Tree Creation Complete for: ", startingPosition, "\nTotal Nodes: ", nodeCount, "\nSolution Nodes: ", len(solvedNodes), "\nRed Esc Nodes:", len(redEscapedNodes)

	printSequence(solvedNodes[0])
	logData()
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
        
    createTree("00200816")






	
	
	






