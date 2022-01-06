import pygame
import sys
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
data = list(map(int, open('data.txt', 'r').read().split()))


def main_menu():
    fon = pygame.transform.scale(pygame.image.load('sprites/fon.png'), size)
    screen.blit(fon, (0, 0))
    text = pygame.transform.scale(pygame.image.load('sprites/labyrinth.png'), (width // 2, height // 6))
    screen.blit(text, (width // 4, height // 6))
    playbtn = pygame.transform.scale(pygame.image.load('sprites/playbtn.png'), (width // 6, height // 6))
    screen.blit(playbtn, ((5 * width) // 12, height // 2))
    quitbtn = pygame.transform.scale(pygame.image.load('sprites/quitbtn.png'), (width // 6, height // 6))
    screen.blit(quitbtn, ((5 * width) // 12, (2 * height) // 3 + height // 100))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if ((5 * width) // 12 <= event.pos[0] <= (7 * width) // 12 and
                        height // 2 <= event.pos[1] <= (2 * height) // 3):
                    return level_menu()
                elif ((5 * width) // 12 <= event.pos[0] <= (7 * width) // 12 and
                      ((2 * height) // 3 + height // 100) <= event.pos[1] <= (
                              2 * height) // 3 + height // 100 + height // 6):
                    pygame.quit()
                    sys.exit()


def level_menu():
    fon = pygame.transform.scale(pygame.image.load('sprites/fon.png'), size)
    screen.blit(fon, (0, 0))

    backbtn = pygame.transform.scale(pygame.image.load('sprites/backbtn.png'), (width // 12, width // 12))
    screen.blit(backbtn, (width // 100, height // 100))

    btn1 = pygame.transform.scale(pygame.image.load('sprites/btn1.png'), (width // 12, width // 12))
    screen.blit(btn1, (3 * width // 24, height // 3))

    if data[0]:
        btn2 = pygame.transform.scale(pygame.image.load('sprites/btn2.png'), (width // 12, width // 12))
    else:
        btn2 = pygame.transform.scale(pygame.image.load('sprites/btn2x.png'), (width // 12, width // 12))
    screen.blit(btn2, (7 * width // 24, height // 3))

    if data[1]:
        btn3 = pygame.transform.scale(pygame.image.load('sprites/btn3.png'), (width // 12, width // 12))
    else:
        btn3 = pygame.transform.scale(pygame.image.load('sprites/btn3x.png'), (width // 12, width // 12))
    screen.blit(btn3, (11 * width // 24, height // 3))

    if data[2]:
        btn4 = pygame.transform.scale(pygame.image.load('sprites/btn4.png'), (width // 12, width // 12))
    else:
        btn4 = pygame.transform.scale(pygame.image.load('sprites/btn4x.png'), (width // 12, width // 12))
    screen.blit(btn4, (15 * width // 24, height // 3))

    if data[3]:
        btn5 = pygame.transform.scale(pygame.image.load('sprites/btn5.png'), (width // 12, width // 12))
    else:
        btn5 = pygame.transform.scale(pygame.image.load('sprites/btn5x.png'), (width // 12, width // 12))
    screen.blit(btn5, (19 * width // 24, height // 3))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (width // 100 <= event.pos[0] <= width // 100 + width // 12 and
                        height // 100 <= event.pos[1] <= height // 100 + width // 12):
                    return main_menu()

                elif (3 * width // 24 <= event.pos[0] <= 3 * width // 24 + width // 12 and
                      height // 3 <= event.pos[1] <= height // 3 + width // 12):
                    return level_1()

                elif (7 * width // 24 <= event.pos[0] <= 7 * width // 24 + width // 12 and
                      height // 3 <= event.pos[1] <= height // 3 + width // 12):
                    return level_2()
                elif (11 * width // 24 <= event.pos[0] <= 11 * width // 24 + width // 12 and
                      height // 3 <= event.pos[1] <= height // 3 + width // 12):
                    return level_3()

                elif (15 * width // 24 <= event.pos[0] <= 15 * width // 24 + width // 12 and
                      height // 3 <= event.pos[1] <= height // 3 + width // 12):
                    return level_4()

                elif (19 * width // 24 <= event.pos[0] <= 19 * width // 24 + width // 12 and
                      height // 3 <= event.pos[1] <= height // 3 + width // 12):
                    return level_5()


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


def level_1():
    pass


def level_2():
    pass


def level_3():
    pass


def level_4():
    pass


def level_5():
    pass


if __name__ == '__main__':
    main_menu()
    ranning = True
    ranning1 = True
    player, max_x, max_y = generate_level(level_map)
    while ranning:
        if win:
            ranning1 = False
            pngwin = pygame.image.load('sprites/win.png')
            pngwin_rect = pngwin.get_rect(
                bottomright=((GetSystemMetrics(0) - GetSystemMetrics(0) // 2) // 2 + GetSystemMetrics(0) // 2,
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
