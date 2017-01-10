import pygame
import mazebuilder
import pathfinder

cellsize = 20
WHITE = (255, 255, 255)
base03 = (0, 43, 54)
base02 = (7, 54, 66)
base01 = (88, 110, 117)
base00 = (101, 123, 131)
base0 = (131, 148, 150)
base1 = (147, 161, 161)
red = (220, 50, 47)
green = (133, 153, 0)
windowSize = (780, 580)	

ppos = (1,0)

maze = mazebuilder.build(mazebuilder.createField(((windowSize[0]/cellsize)/2), ((windowSize[1]/cellsize)/2)))
path = pathfinder.getPath((1,0), (37, 28), maze)
variableWall = path[(len(path)/3)*2]
vx,vy = variableWall
print variableWall
maze[vy][vx] = 'W'
plate = pathfinder.getRandomCorner((1,0), maze)
px,py = plate
maze[py][px] = 'P'
print plate
wallsymbols = ['#', 'W']

pState = 0

pygame.init()
display = pygame.display.set_mode(windowSize)
pygame.display.set_caption('Mazegame v.1')
clock = pygame.time.Clock()

player = pygame.image.load('img/player.png')

def main():
	chrash = False
	while not chrash: #main game loop
		dir = 'WAIT'
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			elif event.type == pygame.KEYDOWN:
				if (event.key == pygame.K_LEFT):
                    			dir = 'LEFT'
                		elif (event.key == pygame.K_RIGHT):
                    			dir = 'RIGHT'
                		elif (event.key == pygame.K_UP):
                    			dir = 'UP'
                		elif (event.key == pygame.K_DOWN):
                    			dir = 'DOWN'
		movePlayer(dir)	
		display.fill(base03)
		drawField()
		drawGrid()
		drawPlayer()
		pygame.display.update()		
		clock.tick(60)

def drawField():
	global maze
	global pState
	for y in range (0, len(maze)):
		for x in range(0, len(maze[y])):
			if maze[y][x] == '#':
				block = pygame.Rect(x*cellsize, y*cellsize, cellsize, cellsize)
				pygame.draw.rect(display, base00, block)
			elif maze[y][x] == 'W':
				block = pygame.Rect(x*cellsize, y*cellsize, cellsize, cellsize)
                                pygame.draw.rect(display, red, block)
			elif maze[y][x] == 'P':
				block = pygame.Rect(x*cellsize, y*cellsize, cellsize, cellsize)
                                pygame.draw.rect(display, green if pState == 0 else red, block)
	 			
def movePlayer(direction):
	global ppos
	x, y = ppos
	global windowSize
	dx, dy = windowSize
	if direction == 'UP' and y > 0:
		if maze[y-1][x] not in wallsymbols:
			ppos = (x,y-1)
	elif direction == 'DOWN' and y < (dy/cellsize)-1:
		if maze[y+1][x] not in wallsymbols:
			ppos = (x,y+1)
	elif direction == 'RIGHT' and x < (dx/cellsize)-1:
		if maze[y][x+1] not in wallsymbols:
			ppos = (x+1,y)
	elif direction == 'LEFT' and x > 0:
		if maze[y][x-1] not in wallsymbols:
			ppos = (x-1,y)
			
def drawPlayer():
	px, py = ppos
	display.blit(player, (px*cellsize,py*cellsize))

def drawGrid():
	global windowSize
	dx, dy = windowSize
	for x in range(0, dx, cellsize):
		pygame.draw.line(display, base00, (x, 0), (x, dy))
	for y in range(0, dy, cellsize):
		pygame.draw.line(display, base00, (0, y), (dx, y))

main()