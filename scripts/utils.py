import pygame

BASE_IMAGE_PATH = 'data/imgs/'


def load_image(fn):
    img = pygame.image.load(BASE_IMAGE_PATH + fn).convert()
    img.set_colorkey((0, 0, 0))
    return img
