import pygame
from pygame import HWSURFACE, DOUBLEBUF, RESIZABLE, VIDEORESIZE

from configuration import Configuration
from level import Level

cfg = Configuration()

pygame.init()
screen_size = (cfg.level_max_height * cfg.sprite_height, cfg.level_max_width * cfg.sprite_width,)
screen = pygame.display.set_mode(screen_size, HWSURFACE | DOUBLEBUF | RESIZABLE)
fake_screen = screen.copy()
pic = pygame.surface.Surface((50, 50))
pic.fill((255, 100, 200))

level = Level()
level.load_from_file('level_0.txt')

clock = pygame.time.Clock()

GAME_FONT = pygame.font.Font(pygame.font.get_default_font(), 12)

current_fps = 0
player_X = 250
player_Y = 250
player_speed_X = 0
player_speed_Y = 0

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == VIDEORESIZE:
            screen = pygame.display.set_mode(event.size, HWSURFACE | DOUBLEBUF | RESIZABLE)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_speed_X = -1
            if event.key == pygame.K_RIGHT:
                player_speed_X = 1
            if event.key == pygame.K_UP:
                player_speed_Y = -1
            if event.key == pygame.K_DOWN:
                player_speed_Y = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_speed_X = 0
            if event.key == pygame.K_RIGHT:
                player_speed_X = 0
            if event.key == pygame.K_UP:
                player_speed_Y = 0
            if event.key == pygame.K_DOWN:
                player_speed_Y = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            mouse_key = pygame.mouse.get_pressed()
            print("Mouse {} {}".format(mouse_pos, mouse_key))

    fake_screen.fill('white')
    level.draw(cfg, fake_screen)
    screen.blit(pygame.transform.scale(fake_screen, screen.get_rect().size), (0, 0))
    pygame.display.flip()

    # player_X += player_speed_X
    # player_Y += player_speed_Y
    #
    # screen.fill((255, 255, 255))
    #
    # pygame.draw.circle(screen, (0, 0, 255), (player_X, player_Y), 75)
    #
    #
    # fps_str = "FPS: " + str(round(clock.get_fps())) + "\r\nPlayer: (" + str(player_X) + ", " + str(player_Y) + ")"
    # text_surface = GAME_FONT.render(fps_str, True, (0, 0, 0))
    # screen.blit(text_surface, (0, 0))
    #
    # pygame.display.flip()

    dt = clock.tick(60)

pygame.quit()
