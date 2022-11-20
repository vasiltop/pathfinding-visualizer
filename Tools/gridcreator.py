import pygame

h, w = input("Enter grid width and height with a space in between: ").split()
h = int(h)
w = int(w)

colors = {
	
	"white" : (255,255,255),
	"blue" : (112, 139, 212),
	"altblue" : (112, 139, 150),
	"green" : (107, 235, 52),
	"pink" : (212, 112, 189),
	"orange" : (252, 186, 3)
}

symbol = {
	
	'#': "pink",
	'p': "altblue",
	's': "orange",
	'e': "green"
}

grid = [["#" for i in range(h)] for j in range(w)]

boxL = int(input("Enter the height/width of each cell: "))
pygame.init()
gameDisplay = pygame.display.set_mode((h * boxL, w * boxL))
pygame.display.set_caption("Maze Editor")
clock = pygame.time.Clock()

running = True

while running:
	for event in pygame.event.get():
		x, y = pygame.mouse.get_pos()
		if(event.type == pygame.QUIT):
			running = False
		if(event.type == pygame.MOUSEBUTTONDOWN):

			if(event.button == 1):
				grid[y // boxL][x // boxL] = "p"
			elif (event.button == 3):
				grid[y // boxL][x // boxL] = "#"

		if event.type == pygame.KEYDOWN:
			if (event.key == pygame.K_s):
				
				for i in range(len(grid)):
					for j in range(len(grid[i])):
						if(grid[i][j] == "s"):
							grid[i][j] = "p"

				grid[y // boxL][x // boxL] = "s"
			if (event.key == pygame.K_e):
				
				for i in range(len(grid)):
					for j in range(len(grid[i])):
						if(grid[i][j] == "e"):
							grid[i][j] = "p"
				grid[y // boxL][x // boxL] = "e"

			if(event.key == pygame.K_ESCAPE):
				running = False

	for i in range(len(grid)):
		for j in range(len(grid[i])):
			pygame.draw.rect(gameDisplay, colors[symbol[grid[i][j]]], (j * boxL, i*boxL, boxL, boxL))
			
	pygame.display.update()
	clock.tick(60)

fileGrid = ["" for i in range(w)]
for i in range(len(grid)):
	for j in range(len(grid[i])):
		fileGrid[i] += grid[i][j]


wfile = open("settings.py", "w")

wfile.write("nodes = " + str(fileGrid) + "\n")
wfile.write("boxL = " + str(boxL) + "\n")
wfile.write("speed = 8" + "\n")
wfile.write("colors = " + str(colors) + "\n")

wfile.close()

pygame.quit()
quit()