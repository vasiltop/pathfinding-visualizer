import math
from settings import colors

class Node:
	def __init__(self, hcost, gcost, fcost, starting, ending, searched, x, y, color, parent):
		self.hcost = hcost #Close to ending point
		self.gcost = gcost #Close to starting point
		self.fcost = fcost #H and G added
		self.starting = starting
		self.ending = ending
		self.searched = searched
		self.x = x
		self.y = y
		self.color = color
		self.parent = parent

class Wall:
	def __init__(self):
		pass

def searchNode(l, y, x, startNode, endNode, parent):
	
	if(type(l[y][x]) != Wall):
		
		if(not l[y][x].searched and not l[y][x].starting):
			
			hcost = round(math.dist([x, y], [endNode.x, endNode.y]))
			gcost = parent.gcost + 1
			fcost = hcost + gcost
			return (hcost, gcost, fcost)
	return -1
	