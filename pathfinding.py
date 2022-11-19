import pygame
from nodes import Node, Wall, searchNode
from text import message_display
from settings import *

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
			updated[i].append(Node(0,0,0, False, False, False, j, i))
		elif(nodes[i][j] == "s"):
			updated[i].append(Node(0,0,0, True, False, False, j, i))
		elif(nodes[i][j] == "e"):
			updated[i].append(Node(0,0,0, False, True, False, j, i))
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

#Running Loop
while running:
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			running = False

	#Drawing Nodes
	gameDisplay.fill((0,0,0))
	for i in range(len(updated)):
		for j in range(len(updated[i])):
			n = updated[i][j]
			if(type(n) == Node):
				if(not n.ending and not n.starting):
					c = colors["blue"]

					if(n.searched): c = colors["altblue"]
					pygame.draw.rect(gameDisplay, c,(j * boxL,i * boxL,boxL,boxL))
					message_display(gameDisplay,f'{round(n.hcost, 1)} , {round(n.gcost, 1)}', ((j * boxL + boxL/2),(i * boxL + boxL/2 - 8)))
					message_display(gameDisplay,f'{n.x}, {n.y}', ((j * boxL + boxL/2),(i * boxL + boxL/2 + 8)))
				elif(n.ending and not n.starting):
					
					
					pygame.draw.rect(gameDisplay, colors["green"],(j * boxL,i * boxL,boxL,boxL))
				elif(not n.ending and n.starting):
					
					pygame.draw.rect(gameDisplay, colors["white"],(j * boxL,i * boxL,boxL,boxL))
			else:
				pygame.draw.rect(gameDisplay, colors["pink"], (j * boxL,i * boxL,boxL,boxL))
	
	

	#Logic
	neighbors = []
	n = updated[y][x]

	#Check if we are at the end node
	if(n.ending): 
		running = False
		print("Completed")

	#Update the list of neighboring nodes
	if(y - 1 >= 0):
		#Check the node above
		if(searchNode(updated, y - 1, x, startNode, endNode, neighbors) != None):
			updated, neighbors = searchNode(updated, y - 1, x, startNode, endNode, neighbors)
	if(x - 1 >= 0):
		#Check the node to the left
		if(searchNode(updated, y, x-1, startNode, endNode, neighbors) != None):
			updated, neighbors = searchNode(updated, y, x-1, startNode, endNode, neighbors)
	if(x + 1 <= len(updated[y]) - 1):
		#Check the node to the right
		if(searchNode(updated, y, x+1, startNode, endNode, neighbors) != None):
			updated, neighbors = searchNode(updated, y, x+1, startNode, endNode, neighbors)
	if(y + 1 <= len(updated) - 1):
		#Check the node below
		if(searchNode(updated, y+1, x, startNode, endNode, neighbors) != None):
			updated, neighbors = searchNode(updated, y+1, x, startNode, endNode, neighbors)
	
	#Find the most optimal node to move to
	if(len(neighbors) != 0):
		bestChoice = neighbors[0]
		fcosts = [i.fcost for i in neighbors]
		if(fcosts.count(fcosts[0]) == len(fcosts) and len(neighbors) >= 2):

			for i in neighbors:
				if(i.hcost < bestChoice.hcost):
					bestChoice = i
		else:
			for i in neighbors:
				if(i.fcost < bestChoice.fcost):
					bestChoice = i
		x = bestChoice.x
		y = bestChoice.y


	#Update display and time
	pygame.display.update()
	clock.tick(speed)


		
				
	
pygame.quit()
quit()