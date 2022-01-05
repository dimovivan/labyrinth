import pygame
from PIL import Image
from win32api import GetSystemMetrics


def image(name, tile_width, tile_height):
    img = Image.open(f'sprites/{name}')
    new_image = img.resize((tile_width, tile_height))
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
tile_width = GetSystemMetrics(0) // 11
tile_height = GetSystemMetrics(1) // 11
level_map = load_level('1.txt')
size = width, height = GetSystemMetrics(0), GetSystemMetrics(1)
win = False

image('wall1.png', tile_width, tile_height)
image('floor1.png', tile_width, tile_height)
image('finish1.png', tile_width, tile_height)
image('1l.png', tile_width // 2, tile_width // 2)
image('2l.png', tile_width // 2, tile_width // 2)
image('3l.png', tile_width // 2, tile_width // 2)
image('1r.png', tile_width // 2, tile_width // 2)
image('2r.png', tile_width // 2, tile_width // 2)
image('3r.png', tile_width // 2, tile_width // 2)
image('1d.png', tile_width // 2, tile_width // 2)
image('2d.png', tile_width // 2, tile_width // 2)
image('3d.png', tile_width // 2, tile_width // 2)
image('1u.png', tile_width // 2, tile_width // 2)
image('2u.png', tile_width // 2, tile_width // 2)
image('3u.png', tile_width // 2, tile_width // 2)
image('win.png', GetSystemMetrics(0) // 2, GetSystemMetrics(1) // 10)

tile_images = {
    'wall': pygame.image.load('sprites/wall1.png'),
    'floor': pygame.image.load('sprites/floor1.png'),
    'finish': pygame.image.load('sprites/finish1.png'),
}
player_sprite = \
    [[pygame.image.load('sprites/1l.png'), pygame.image.load('sprites/2l.png'), pygame.image.load('sprites/3l.png')],
     [pygame.image.load('sprites/1r.png'), pygame.image.load('sprites/2r.png'), pygame.image.load('sprites/3r.png')],
     [pygame.image.load('sprites/1d.png'), pygame.image.load('sprites/2d.png'), pygame.image.load('sprites/3d.png')],
     [pygame.image.load('sprites/1u.png'), pygame.image.load('sprites/2u.png'), pygame.image.load('sprites/3u.png')]]
t = 0
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
pngwin = pygame.image.load('sprites/win.png')
pngwin_rect = pngwin.get_rect(bottomright=((GetSystemMetrics(0) - GetSystemMetrics(0) // 2) // 2,
                                           (GetSystemMetrics(1) - GetSystemMetrics(1) // 10) // 2))
screen = pygame.display.set_mode(size)


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    global t

    def __init__(self, pos_x, pos_y):
        super().__init__(player_group)
        self.image = player_sprite[0][t]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + tile_width // 3.3, tile_height * pos_y + tile_height // 10)
        self.pos = (pos_x, pos_y)

    def move(self, x, y, x1, y1, n):
        global t
        self.pos = (x1, y1)
        self.rect = self.image.get_rect().move(x,
                                               y)
        t += 1
        if t == 3:
            t = 0
        self.image = player_sprite[n][t]


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
            elif level[y][x] == '?':
                Tile('floor', x, y)
                new_player = Player(x, y)
    return new_player, x, y


def move(hero, movement):
    global win, ranning
    x, y = hero.pos
    x1, y1 = hero.rect[0], hero.rect[1]
    if movement == 'up':
        if y > 0 and level_map[y - 1][x] == '@':
            hero.move(x1, y1 - tile_height, x, y - 1, 3)
            win = True
        elif y > 0 and level_map[y - 1][x] != '#':
            hero.move(x1, y1 - tile_height, x, y - 1, 3)

    elif movement == 'down':
        if y < max_y - 1 and level_map[y + 1][x] == '@':
            hero.move(x1, y1 + tile_height, x, y + 1, 2)
            win = True
        elif y < max_y - 1 and level_map[y + 1][x] != '#':
            hero.move(x1, y1 + tile_height, x, y + 1, 2)
    elif movement == 'left':
        if x > 0 and level_map[y][x - 1] == '@':
            hero.move(x1 - tile_width, y1, x - 1, y, 0)
            win = True
        elif x > 0 and level_map[y][x - 1] != '#':
            hero.move(x1 - tile_width, y1, x - 1, y, 0)
    elif movement == 'right':
        if x < max_x - 1 and level_map[y][x + 1] == '@':
            hero.move(x1 + tile_width, y1, x + 1, y, 1)
            win = True
        elif x < max_x - 1 and level_map[y][x + 1] != '#':
            hero.move(x1 + tile_width, y1, x + 1, y, 1)


if __name__ == '__main__':
    ranning = True
    ranning1 = True
    player, max_x, max_y = generate_level(level_map)
    while ranning:
        if win:
            ranning1 = False
            pngwin = pygame.image.load('sprites/win.png')
            pngwin_rect = pngwin.get_rect(bottomright=((GetSystemMetrics(0) - GetSystemMetrics(0) // 2) // 2 + GetSystemMetrics(0) // 2,
                                                       (GetSystemMetrics(1) - GetSystemMetrics(1) // 10) // 2 + GetSystemMetrics(1) // 10))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ranning = False
            screen.blit(pngwin, pngwin_rect)
            pygame.display.update()
        if ranning1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ranning = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        move(player, 'up')
                    if event.key == pygame.K_DOWN:
                        move(player, 'down')
                    if event.key == pygame.K_RIGHT:
                        move(player, 'right')
                    if event.key == pygame.K_LEFT:
                        move(player, 'left')
            screen.fill(pygame.Color('black'))
            tiles_group.draw(screen)
            player_group.draw(screen)
            pygame.display.flip()
    pygame.quit()