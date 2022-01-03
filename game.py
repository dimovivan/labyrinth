import pygame
import sys
from PIL import Image


def image(name, tile_width):
    img = Image.open(f'sprites/{name}')
    new_image = img.resize((tile_width, tile_width))
    new_image.save(f'sprites/{name}')


def load_level(filename):
    filename = "level/" + filename
    try:
        with open(filename, 'r') as mapFile:
            level_map = [line.strip() for line in mapFile]

            max_width = max(map(len, level_map))

        return list(map(lambda x: x.ljust(max_width, '.'), level_map))
    except BaseException:
        return 0


pygame.init()
tile_width = tile_height = 50
level_map = load_level('1.txt')
size = width, height = 500, 500
image('wall1.png', tile_width)
image('floor1.png', tile_width)
image('finish1.png', tile_width)
tile_images = {
    'wall': pygame.image.load('sprites/wall1.png'),
    'floor': pygame.image.load('sprites/floor1.png'),
    'finish': pygame.image.load('sprites/finish1.png'),
}
tiles_group = pygame.sprite.Group()
screen = pygame.display.set_mode(size)


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('floor', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('finish', x, y)
    return new_player, x, y


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    ranning = True
    player, max_x, max_y = generate_level(level_map)
    while ranning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ranning = False
        screen.fill(pygame.Color('black'))
        tiles_group.draw(screen)
        pygame.display.flip()
    pygame.quit()