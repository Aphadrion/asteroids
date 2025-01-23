import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
import sys

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()

	print("Starting asteroids!")
	#print(f"Screen width: {SCREEN_WIDTH}")
	#print(f"Screen height: {SCREEN_HEIGHT}")
	
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = updatable
	field = AsteroidField()

	Shot.containers = (shots, updatable, drawable)

	Player.containers = (updatable, drawable)
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	player = Player(x,y)
	
	dt = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
				
		
		for obj in updatable:	
			obj.update(dt)

		screen.fill("black")

		for obj in drawable:
			obj.draw(screen)

		for obj in asteroids:
			if obj.collision(player) == True:
				return sys.exit("Game Over!")
			
		for ast in asteroids:
			for shot in shots:
				if shot.collision(ast):
					ast.split()

		pygame.display.flip()
		dt = clock.tick(60) / 1000
		
if __name__ == "__main__":
    main()
