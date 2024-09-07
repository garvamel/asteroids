import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_clock = pygame.time.Clock()
    dt = 0


    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfiled = AsteroidField()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        
        for updt in updatables:
            updt.update(dt)
        for drw in drawables:
            drw.draw(screen)
        for astrd in asteroids:
            if astrd.check_collision(player):
                print("Game over!")
                sys.exit()
            for sht in shots:
                if sht.check_collision(astrd):
                    sht.kill()
                    astrd.split()
        
        pygame.display.flip()
        dt = game_clock.tick(60)/1000
        
if __name__ == "__main__":
    main()
