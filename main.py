# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shots import Shot

def main():
    print("Starting Asteroids!")
    
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    # Sprite Containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Static container properties
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    # Initialize game objects
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroidField = AsteroidField()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))

        updatable.update(dt)

        for item in drawable:
            item.draw(screen)

        for asteroid in asteroids:
            if asteroid.hasCollided(player):
                print("Collision Detected, Game Over!")
                raise SystemExit

        dt = clock.tick(60) / 1000
        
        #call this last
        pygame.display.flip()


if __name__ == "__main__":
    main()
