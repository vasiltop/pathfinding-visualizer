import math
class Node:
	def __init__(self, hcost, gcost, fcost, starting, ending, searched, x, y):
		self.hcost = hcost #Close to ending point
		self.gcost = gcost #Close to starting point
		self.fcost = fcost #H and G added
		self.starting = starting
		self.ending = ending
		self.searched = searched
		self.x = x
		self.y = y

class Wall:
	def __init__(self):
		pass

def searchNode(l, y, x, startNode, endNode, neighbors):
	ol = l
	on = neighbors
	if(type(l[y][x]) != Wall and not l[y][x].searched and not l[y][x].starting):
		
		l[y][x].hcost = round(math.dist([x, y], [endNode.x, endNode.y]))
		l[y][x].gcost = round(math.dist([x, y], [startNode.x, startNode.y]))
		l[y][x].fcost = l[y][x].hcost + l[y][x].gcost
		l[y][x].searched = True
		
		neighbors.append(l[y][x])

		return (l, neighbors)
	return (ol, on)