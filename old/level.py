import pygame.draw

from configuration import Configuration


class Level:
    lines = 0
    rows = 0
    cells = []

    color_wall = (0, 0, 0)
    color_space = (100, 100, 100)

    def load_from_file(self, fn):
        self.lines = 0
        self.rows = 0
        self.cells = []
        with open(fn) as f:
            for line in f.readlines():
                row = []
                for char in line.strip():
                    row.append(char)
                if (len(row)) > self.rows:
                    self.rows = len(row)
                self.cells.append(row)
                self.lines += 1
        return

    def draw(self, cfg: Configuration, screen):
        for y in range(self.lines):
            for x in range(self.rows):
                cell = self.cells[y][x]
                rect = pygame.rect.Rect(
                    x * cfg.sprite_width, y * cfg.sprite_height,
                    cfg.sprite_width, cfg.sprite_height
                )
                match cell:
                    case 'X':
                        pygame.draw.rect(screen, self.color_wall, rect)
                    case '_':
                        pygame.draw.rect(screen, self.color_space, rect)
