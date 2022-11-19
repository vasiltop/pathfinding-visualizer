import pygame
import math
boxL = 64
pygame.init()


nodes = [
"############s###",
"#ppppp#ppppppp##",
"ep###pppp###pp##",
"#p###pp#p##ppp##",
"#pppp##pp##ppp##",
"####p###########",
"###pp###ppppppp#",
"####ppppp#######",
"########pp####pp",
"########ppppppp#",
"################"
]



l = len(nodes)
w = len(nodes[0])



updated = []


gameDisplay = pygame.display.set_mode((w * boxL,l * boxL))
pygame.display.set_caption("Pathfinder")
clock = pygame.time.Clock()
white = (255,255,255)
blue = (112, 139, 212)
altblue = (112, 139, 150)
green = (107, 235, 52)
pink = (212, 112, 189)
endNode = None
startNode = None
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
def text_objects(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()

def message_display(text, center):
    largeText = pygame.font.Font('freesansbold.ttf', 12)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (center)
    gameDisplay.blit(TextSurf, TextRect)




running = True





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
					c = blue

					if(n.searched): c = altblue
					pygame.draw.rect(gameDisplay, c,(j * boxL,i * boxL,boxL,boxL))
					message_display(f'{round(n.hcost, 1)} , {round(n.gcost, 1)}', ((j * boxL + boxL/2),(i * boxL + boxL/2 - 8)))
					message_display(f'{n.x}, {n.y}', ((j * boxL + boxL/2),(i * boxL + boxL/2 + 8)))
				elif(n.ending and not n.starting):
					
					
					pygame.draw.rect(gameDisplay, green,(j * boxL,i * boxL,boxL,boxL))
				elif(not n.ending and n.starting):
					
					pygame.draw.rect(gameDisplay, white,(j * boxL,i * boxL,boxL,boxL))
			else:
				pygame.draw.rect(gameDisplay, pink, (j * boxL,i * boxL,boxL,boxL))
	neighbors = []
	print(x, y)
	def searchNode(y, x):
		if(type(updated[y][x]) != Wall and not updated[y][x].searched and not updated[y][x].starting):
			
			updated[y][x].hcost = round(math.dist([x, y], [endNode.x, endNode.y]))
			updated[y][x].gcost = round(math.dist([x, y], [startNode.x, startNode.y]))
			updated[y][x].fcost = updated[y][x].hcost + updated[y][x].gcost
			updated[y][x].searched = True
			
			neighbors.append(updated[y][x])
	#Logic
	n = updated[y][x]

	if(n.ending): 
		running = False
		print("Completed")
	if(y - 1 >= 0):
		#check up
		searchNode(y - 1, x)
	
	if(x - 1 >= 0):
		#check left
		searchNode(y, x-1)
	if(x + 1 <= len(updated[y]) - 1):
		#check right
	
		searchNode(y, x+1)
		

	if(y + 1 <= len(updated) - 1):
		#check down
		searchNode(y+1, x)
	

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

	pygame.display.update()
	clock.tick(1)


		
				
	
pygame.quit()
quit()