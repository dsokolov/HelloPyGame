import pygame

NEIGHBOR_OFFSETS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 0), (0, 1),
    (1, -1), (1, 0), (1, 1)
]
PHYSICS_TILES = {'wall'}


class Tilemap:
    def __init__(self, game, tile_size=32):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = {}

        # for i in range(5):
        #     self.tilemap[str(1 + i) + ';4'] = {'type': 'wall', 'variant': 2, 'pos': (1 + i, 4)}

        self.tilemap['0;4'] = {'type': 'wall', 'variant': 1, 'pos': (0, 4)}
        self.tilemap['1;4'] = {'type': 'wall', 'variant': 1, 'pos': (1, 4)}
        self.tilemap['2;4'] = {'type': 'wall', 'variant': 1, 'pos': (2, 4)}
        self.tilemap['3;4'] = {'type': 'wall', 'variant': 1, 'pos': (3, 4)}
        self.tilemap['4;4'] = {'type': 'wall', 'variant': 0, 'pos': (4, 4)}
        self.tilemap['5;5'] = {'type': 'wall', 'variant': 1, 'pos': (5, 5)}
        self.tilemap['6;5'] = {'type': 'wall', 'variant': 1, 'pos': (6, 5)}
        self.tilemap['7;5'] = {'type': 'wall', 'variant': 1, 'pos': (7, 5)}
        self.tilemap['8;5'] = {'type': 'wall', 'variant': 1, 'pos': (8, 5)}

        self.tilemap['6;2'] = {'type': 'wall', 'variant': 1, 'pos': (6, 2)}
        self.tilemap['7;2'] = {'type': 'wall', 'variant': 1, 'pos': (7, 2)}

    def tiles_around(self, pos):
        tiles = []
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        for offset in NEIGHBOR_OFFSETS:
            check_loc_x = tile_loc[0] + offset[0]
            check_loc_y = tile_loc[1] + offset[1]
            check_loc = "{};{}".format(check_loc_x, check_loc_y)
            if check_loc in self.tilemap:
                tile = self.tilemap[check_loc]
                tiles.append(tile)
        return tiles

    def physic_rects_around(self, pos):
        rects = []
        for tile in self.tiles_around(pos):
            if tile['type'] in PHYSICS_TILES:
                x = tile['pos'][0] * self.tile_size
                y = tile['pos'][1] * self.tile_size
                rect = pygame.Rect(x, y, self.tile_size, self.tile_size)
                rects.append(rect)
        return rects

    def render(self, surface):
        for loc in self.tilemap:
            tile = self.tilemap[loc]
            asset = self.game.assets[tile['type']]
            img = asset[tile['variant']]
            pos = (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size)
            surface.blit(img, pos)
