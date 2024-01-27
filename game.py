import sys

import pygame
from scripts.entities import PhysicsEntity
from scripts.utils import load_image


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("my game")
        self.screen = pygame.display.set_mode((800, 600))
        self.display = pygame.Surface((320, 240))
        self.clock = pygame.time.Clock()
        self.movement = [False, False]
        self.player = PhysicsEntity(self, 'player', (10, 10), (32, 32))
        self.assets = {
            'player': load_image('blue_ball.png')
        }

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False

            self.player.update((self.movement[1] - self.movement[0], 0))

            self.display.fill('gray')
            self.player.render(self.display)

            transformed_display = pygame.transform.scale(self.display, self.screen.get_size())
            self.screen.blit(transformed_display, (0, 0))
            pygame.display.update()
            self.clock.tick(60)


game = Game()
game.run()
