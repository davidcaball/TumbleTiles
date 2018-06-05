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




board = TT.board

