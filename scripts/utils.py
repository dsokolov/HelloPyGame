import pygame
import os

BASE_IMAGE_PATH = 'data/images/'


def load_image(fn):
    img = pygame.image.load(BASE_IMAGE_PATH + fn).convert()
    # img.set_colorkey((143, 222, 93))
    img.set_colorkey((0, 0, 0, 0))
    return img


def load_images(path):
    images = []
    for fn in os.listdir(BASE_IMAGE_PATH + path):
        image = load_image(path + fn)
        images.append(image)
    return images
