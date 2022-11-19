import pygame
from nodes import Node, Wall, searchNode
from text import message_display
from settings import *
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

#Initialization
pygame.init()
l = len(nodes)
w = len(nodes[0])
updated = []
gameDisplay = pygame.display.set_mode((w * boxL,l * boxL))
pygame.display.set_caption("Pathfinder")
clock = pygame.time.Clock()
endNode = None
startNode = None
running = True

#Create updated grid of nodes
for i in range(len(nodes)):
	updated.append([])
	for j in range(len(nodes[i])):
		if(nodes[i][j] == "p"):
			updated[i].append(Node(0,0,0, False, False, False, j, i, colors["altblue"], None))
		elif(nodes[i][j] == "s"):
			updated[i].append(Node(0,0,0, True, False, True, j, i, colors["orange"], None))
		elif(nodes[i][j] == "e"):
			updated[i].append(Node(0,0,0, False, True, False, j, i, colors["green"], None))
		elif(nodes[i][j] == "#"):
			updated[i].append(Wall())

#Find start and end node's positions
for i in range(len(updated)):
	for j in range(len(updated[i])):
		n = updated[i][j]
		if(type(n) == Node):
			if(n.ending):
				endNode = n
			if(n.starting):
				startNode = n
				x = startNode.x
				y = startNode.y
searching = True
index = endNode
#Running Loop
while running:
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			running = False

	#Drawing Nodes
	gameDisplay.fill(colors["pink"])
	for i in range(len(updated)):
		for j in range(len(updated[i])):
			n = updated[i][j]
			if(type(n) == Node):
				if(not n.ending and not n.starting):
					pygame.draw.rect(gameDisplay, n.color,(j * boxL,i * boxL,boxL,boxL))
					message_display(gameDisplay,f'{round(n.hcost, 1)} , {round(n.gcost, 1)}', ((j * boxL + boxL/2),(i * boxL + boxL/2 - 8)))
					message_display(gameDisplay,f'{n.x}, {n.y}', ((j * boxL + boxL/2),(i * boxL + boxL/2 + 8)))
				elif(n.ending and not n.starting):
					pygame.draw.rect(gameDisplay, n.color,(j * boxL,i * boxL,boxL,boxL))
				elif(not n.ending and n.starting):
					pygame.draw.rect(gameDisplay, n.color,(j * boxL,i * boxL,boxL,boxL))
	

	#Logic
	searchedNodes = []
	nodesToChooseFrom = []

	for i in range(len(updated)):
		for j in range(len(updated[i])):
			if(type(updated[i][j]) == Node):
				if(updated[i][j].searched == True):
					searchedNodes.append(updated[i][j])
	
	for i in searchedNodes:
		

		if(searching):
			if(i.y > 0):
				
				rs = searchNode(updated, i.y - 1, i.x, startNode, endNode, i)

				if(rs != -1):
					updated[i.y-1][i.x].parent = i
					updated[i.y-1][i.x].hcost = rs[0]
					updated[i.y-1][i.x].gcost = rs[1]
					updated[i.y-1][i.x].fcost = rs[2]
					updated[i.y-1][i.x].parent = i
					nodesToChooseFrom.append(updated[i.y-1][i.x])

			if(i.y < (l - 1)):
				
				rs = searchNode(updated, i.y + 1, i.x, startNode, endNode, i)
				print(i.x, i.y+1)
				if(rs != -1):
					updated[i.y+1][i.x].parent = i
					updated[i.y+1][i.x].hcost = rs[0]
					updated[i.y+1][i.x].gcost = rs[1]
					updated[i.y+1][i.x].fcost = rs[2]
					updated[i.y+1][i.x].parent = i
					nodesToChooseFrom.append(updated[i.y+1][i.x])
			if(i.x > 0):
				
				rs = searchNode(updated, i.y, i.x - 1, startNode, endNode, i)
				if(rs != -1):
					updated[i.y][i.x - 1].parent = i
					updated[i.y][i.x - 1].hcost = rs[0]
					updated[i.y][i.x - 1].gcost = rs[1]
					updated[i.y][i.x - 1].fcost = rs[2]
					updated[i.y][i.x - 1].parent = i
					nodesToChooseFrom.append(updated[i.y][i.x - 1])
			if(i.x < (w - 1)):
				
				rs = searchNode(updated, i.y, i.x + 1, startNode, endNode, i)
				if(rs != -1):
					updated[i.y][i.x + 1].hcost = rs[0]
					updated[i.y][i.x + 1].gcost = rs[1]
					updated[i.y][i.x + 1].fcost = rs[2]
					updated[i.y][i.x + 1].parent = i
					nodesToChooseFrom.append(updated[i.y][i.x + 1])
			

			if(endNode not in nodesToChooseFrom): 

				if(len(nodesToChooseFrom) > 0):
					low = nodesToChooseFrom[0]
					mn = nodesToChooseFrom[0].fcost

					for i in nodesToChooseFrom:

						
						if(i.fcost < mn):
							mn = i.fcost
							low = i

					low.searched = True
					
					low.color = colors['blue']

					for i in nodesToChooseFrom:
						updated[low.y][low.x] = low
			else:
				searching = False


	if(not searching):
		
		p = index.parent
		
		if(p != None ):
			if(index != endNode):
				index.color = colors["white"]
			index = p

	#Update display, time and background
	
	pygame.display.update()
	clock.tick(speed)

pygame.quit()
quit()