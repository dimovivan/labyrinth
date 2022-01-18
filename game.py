import pygame
import sys
from PIL import Image
from win32api import GetSystemMetrics
import random


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
tile_width = GetSystemMetrics(0) // 20
tile_height = GetSystemMetrics(1) // 20
clock = pygame.time.Clock()
size = width, height = GetSystemMetrics(0), GetSystemMetrics(1)
star_sprites = pygame.sprite.Group()
fire_sprites = pygame.sprite.Group()
fire_pos = []
screen_rect = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))

image('wall1.png', tile_width, tile_height)
image('floor1.png', tile_width, tile_height)
image('finish1.png', tile_width, tile_height)
image('trap1.png', tile_width, tile_height)
image('trap3.png', tile_width, tile_height)
image('fire1.png', tile_width // 3, tile_height // 2)
image('trap2.png', tile_width, tile_height)
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
image('game_over.png', GetSystemMetrics(0) // 2, GetSystemMetrics(1) // 10)

tile_images = {
    'wall': pygame.image.load('sprites/wall1.png'),
    'floor': pygame.image.load('sprites/floor1.png'),
    'finish': pygame.image.load('sprites/finish1.png'),
    'trap': pygame.image.load('sprites/trap1.png'),
    'trap1': pygame.image.load('sprites/trap2.png'),
    'trap2': pygame.image.load('sprites/trap3.png')
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
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return main_menu()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (width // 100 <= event.pos[0] <= width // 100 + width // 12 and
                        height // 100 <= event.pos[1] <= height // 100 + width // 12):
                    return main_menu()

                elif (3 * width // 24 <= event.pos[0] <= 3 * width // 24 + width // 12 and
                      height // 3 <= event.pos[1] <= height // 3 + width // 12):
                    return level(1)

                elif (7 * width // 24 <= event.pos[0] <= 7 * width // 24 + width // 12 and
                      height // 3 <= event.pos[1] <= height // 3 + width // 12) and data[0]:
                    return level(2)

                elif (11 * width // 24 <= event.pos[0] <= 11 * width // 24 + width // 12 and
                      height // 3 <= event.pos[1] <= height // 3 + width // 12) and data[1]:
                    return level(3)

                elif (15 * width // 24 <= event.pos[0] <= 15 * width // 24 + width // 12 and
                      height // 3 <= event.pos[1] <= height // 3 + width // 12) and data[2]:
                    return level(4)

                elif (19 * width // 24 <= event.pos[0] <= 19 * width // 24 + width // 12 and
                      height // 3 <= event.pos[1] <= height // 3 + width // 12) and data[3]:
                    return level(5)


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


class fire(pygame.sprite.Sprite):
    fire = [pygame.image.load("sprites/fire1.png")]

    def __init__(self, pos, dx, dy):
        super().__init__(fire_sprites)
        self.image = self.fire[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velocity = [dx, dy]

    def update(self, hero):
        global game_over, fire_game_over, fon_music
        x, y = hero.pos
        self.rect.y += self.velocity[1]
        if not self.rect.colliderect(screen_rect):
            self.kill()
        if y * tile_height - tile_height // 4 < self.rect.y < y * tile_height and self.rect.x // tile_width == x:
            fire_game_over = True
            game_over = True
            fon_music.stop()
            fon_music = pygame.mixer.Sound('soundtreck/game_over.mp3')
            fon_music.play()


def create_particles(position, sb):
    if sb == 0 or sb == 1:
        if sb == 0:
            particle_count = 20
            numbers = range(-5, 6)
        elif sb == 1:
            particle_count = 3
            numbers = range(-2, 3)
        for _ in range(particle_count):
            Particle(position, random.choice(numbers), random.choice(numbers), sb)
    else:
        fire(position, 0, tile_height // 4)


class Particle(pygame.sprite.Sprite):
    fire = []
    fire1 = [pygame.image.load("sprites/star.png")]
    for scale in (5, 10, 20):
        fire1.append(pygame.transform.scale(fire1[0], (scale, scale)))
    fire2 = [pygame.image.load("sprites/blood1.png")]
    for scale in (5, 10, 20):
        fire2.append(pygame.transform.scale(fire2[0], (scale, scale)))
    fire.append(fire1)
    fire.append(fire2)

    def __init__(self, pos, dx, dy, t):
        super().__init__(star_sprites)
        self.image = random.choice(self.fire[t])
        self.rect = self.image.get_rect()
        self.t = t
        self.x = 0

        self.velocity = [dx, dy]
        self.rect.x, self.rect.y = pos
        if t == 0:
            self.gravity = 0.04
        else:
            self.gravity = 0.1

    def update(self):
        self.velocity[1] += self.gravity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        self.x += 1
        if self.t == 1 and self.x > 20:
            self.kill()
        if not self.rect.colliderect(screen_rect):
            self.kill()


def generate_level(level):
    global fire_pos
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('floor', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '!':
                Tile('trap', x, y)
            elif level[y][x] == '*':
                Tile('trap2', x, y)
                fire_pos.append((x * tile_width + tile_width // 3, y * tile_height + tile_height // 2))
            elif level[y][x] == '@':
                Tile('finish', x, y)
            elif level[y][x] == '?':
                Tile('floor', x, y)
                new_player = Player(x, y)
    return new_player, x, y


def move(hero, movement):
    global win, game_over, fon_music
    x, y = hero.pos
    x1, y1 = hero.rect[0], hero.rect[1]
    if movement == 'up':
        if y > 0 and level_map[y - 1][x] == '@':
            hero.move(x1, y1 - tile_height, x, y - 1, 3)
            win = True
            fon_music.stop()
            fon_music = pygame.mixer.Sound('soundtreck/win.mp3')
            fon_music.play()
        elif y > 0 and level_map[y - 1][x] == '!':
            hero.move(x1, y1 - tile_height, x, y - 1, 3)
            game_over = True
            fon_music.stop()
            fon_music = pygame.mixer.Sound('soundtreck/game_over.mp3')
            fon_music.play()
            Tile('floor', x, y - 1)
        elif y > 0 and level_map[y - 1][x] not in ['#', '*']:
            hero.move(x1, y1 - tile_height, x, y - 1, 3)
    elif movement == 'down':
        if y < max_y - 1 and level_map[y + 1][x] == '@':
            hero.move(x1, y1 + tile_height, x, y + 1, 2)
            win = True
            fon_music.stop()
            fon_music = pygame.mixer.Sound('soundtreck/win.mp3')
            fon_music.play()
        elif y < max_y - 1 and level_map[y + 1][x] == '!':
            hero.move(x1, y1 + tile_height, x, y + 1, 2)
            game_over = True
            fon_music.stop()
            fon_music = pygame.mixer.Sound('soundtreck/game_over.mp3')
            fon_music.play()
            Tile('floor', x, y + 1)
        elif y < max_y - 1 and level_map[y + 1][x] not in ['#', '*']:
            hero.move(x1, y1 + tile_height, x, y + 1, 2)
    elif movement == 'left':
        if x > 0 and level_map[y][x - 1] == '@':
            hero.move(x1 - tile_width, y1, x - 1, y, 0)
            win = True
            fon_music.stop()
            fon_music = pygame.mixer.Sound('soundtreck/win.mp3')
            fon_music.play()
        elif x > 0 and level_map[y][x - 1] == '!':
            hero.move(x1 - tile_width, y1, x - 1, y, 0)
            game_over = True
            fon_music.stop()
            fon_music = pygame.mixer.Sound('soundtreck/game_over.mp3')
            fon_music.play()
            Tile('floor', x - 1, y)
        elif x > 0 and level_map[y][x - 1] not in ['#', '*']:
            hero.move(x1 - tile_width, y1, x - 1, y, 0)
    elif movement == 'right':
        if x < max_x - 1 and level_map[y][x + 1] == '@':
            hero.move(x1 + tile_width, y1, x + 1, y, 1)
            win = True
            fon_music.stop()
            fon_music = pygame.mixer.Sound('soundtreck/win.mp3')
            fon_music.play()
        elif x < max_x - 1 and level_map[y][x + 1] == '!':
            hero.move(x1 + tile_width, y1, x + 1, y, 1)
            game_over = True
            fon_music.stop()
            fon_music = pygame.mixer.Sound('soundtreck/game_over.mp3')
            fon_music.play()
            Tile('floor', x + 1, y)
        elif x < max_x - 1 and level_map[y][x + 1] not in ['#', '*']:
            hero.move(x1 + tile_width, y1, x + 1, y, 1)


def pause():
    tiles_group.draw(screen)
    player_group.draw(screen)
    fire_sprites.draw(screen)
    text = pygame.transform.scale(pygame.image.load('sprites/pause.png'), (width // 2, height // 6))
    screen.blit(text, (width // 4, height // 6))
    restartbtn = pygame.transform.scale(pygame.image.load('sprites/restartbtn.png'), (width // 6, height // 6))
    screen.blit(restartbtn, ((5 * width) // 12, height // 2))
    menubtn = pygame.transform.scale(pygame.image.load('sprites/menubtn.png'), (width // 6, height // 6))
    screen.blit(menubtn, ((5 * width) // 12, (2 * height) // 3 + height // 100))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if ((5 * width) // 12 <= event.pos[0] <= (7 * width) // 12 and
                        height // 2 <= event.pos[1] <= (2 * height) // 3):
                    return 'restart'
                elif ((5 * width) // 12 <= event.pos[0] <= (7 * width) // 12 and
                      ((2 * height) // 3 + height // 100) <= event.pos[1] <= (
                              2 * height) // 3 + height // 100 + height // 6):
                    return 'menu'
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return


def level(level_number):
    global level_map, max_x, max_y, pngwin, win, game_over, fire_game_over, fon_music, fire_pos
    tiles_group.empty()
    player_group.empty()
    star_sprites.empty()
    fire_sprites.empty()
    fire_pos = []
    try:
        fon_music.stop()
    except BaseException:
        pass
    level_map = load_level(f'{level_number}.txt')
    ranning = True
    ranning1 = True
    win = False
    game_over = False
    fire_game_over = False
    player, max_x, max_y = generate_level(level_map)
    pygame.mixer.music.load('soundtreck/fon.mp3')
    fon_music = pygame.mixer.Sound('soundtreck/fon.mp3')
    fire_time = 0
    fon_music.play(-1)
    while ranning:
        if win:
            screen.fill((0, 0, 0))
            tiles_group.draw(screen)
            player_group.draw(screen)
            ranning1 = False
            pngwin = pygame.image.load('sprites/win.png')
            pngwin_rect = pngwin.get_rect(
                bottomright=((GetSystemMetrics(0) - GetSystemMetrics(0) // 2) // 2 + GetSystemMetrics(0) // 2,
                             (GetSystemMetrics(1) - GetSystemMetrics(1) // 10) // 2 + GetSystemMetrics(1) // 10))
            restartbtn = pygame.transform.scale(pygame.image.load('sprites/restartbtn.png'), (width // 6, height // 6))
            screen.blit(restartbtn, ((5 * width) // 12, 3 * height // 5))
            menubtn = pygame.transform.scale(pygame.image.load('sprites/menubtn.png'), (width // 6, height // 6))
            screen.blit(menubtn, ((5 * width) // 12, 4 * height // 5))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ranning = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if ((5 * width) // 12 <= event.pos[0] <= (7 * width) // 12 and
                            3 * height // 5 <= event.pos[1] <= (23 * height) // 30):
                        screen.fill((0, 0, 0))
                        return level(level_number)
                    elif ((5 * width) // 12 <= event.pos[0] <= (7 * width) // 12 and
                          4 * height // 5 <= event.pos[1] <= (29 * height) // 30):
                        fon_music.stop()
                        return main_menu()
            create_particles((-10, GetSystemMetrics(1)), 0)
            create_particles((GetSystemMetrics(0), GetSystemMetrics(1)), 0)
            screen.blit(pngwin, pngwin_rect)
            star_sprites.update()
            star_sprites.draw(screen)
            if level_number != 5:
                with open('data.txt', 'w') as file:
                    data[level_number - 1] = 1
                    file.write(' '.join(map(str, data)))
            pygame.display.flip()
            pygame.display.update()
            clock.tick(50)
        elif game_over:
            screen.fill((0, 0, 0))
            tiles_group.draw(screen)
            ranning1 = False
            player_group.draw(screen)
            pnggame_over = pygame.image.load('sprites/game_over.png')
            pnggame_over_rect = pngwin.get_rect(
                bottomright=((GetSystemMetrics(0) - GetSystemMetrics(0) // 2) // 2 + GetSystemMetrics(0) // 2,
                             (GetSystemMetrics(1) - GetSystemMetrics(1) // 10) // 2 + GetSystemMetrics(1) // 10))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ranning = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if ((5 * width) // 12 <= event.pos[0] <= (7 * width) // 12 and
                            3 * height // 5 <= event.pos[1] <= (23 * height) // 30):
                        screen.fill((0, 0, 0))
                        return level(level_number)
                    elif ((5 * width) // 12 <= event.pos[0] <= (7 * width) // 12 and
                          4 * height // 5 <= event.pos[1] <= (29 * height) // 30):
                        fon_music.stop()
                        return main_menu()
            screen.blit(pnggame_over, pnggame_over_rect)

            if fire_game_over:
                fire_sprites.draw(screen)
            else:
                create_particles(
                    (player.pos[0] * tile_width + tile_width // 2, player.pos[1] * tile_height + tile_height // 2), 1)
                screen.blit(pygame.image.load('sprites/trap2.png'),
                            (player.pos[0] * tile_width, player.pos[1] * tile_height))
                star_sprites.update()
                star_sprites.draw(screen)
            restartbtn = pygame.transform.scale(pygame.image.load('sprites/restartbtn.png'), (width // 6, height // 6))
            screen.blit(restartbtn, ((5 * width) // 12, 3 * height // 5))
            menubtn = pygame.transform.scale(pygame.image.load('sprites/menubtn.png'), (width // 6, height // 6))
            screen.blit(menubtn, ((5 * width) // 12, 4 * height // 5))
            pygame.display.flip()
            pygame.display.update()
            clock.tick(50)
        if ranning1:
            screen.fill((0, 0, 0))
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
                    if event.key == pygame.K_ESCAPE:
                        x = pause()
                        if x == 'restart':
                            return level(level_number)
                        elif x == 'menu':
                            fon_music.stop()
                            return main_menu()
            tiles_group.draw(screen)
            player_group.draw(screen)
            if fire_time % 70 == 0:
                for i in fire_pos:
                    create_particles((i[0], i[1]), 2)
            fire_sprites.update(player)
            fire_sprites.draw(screen)
            pygame.display.flip()
            screen.fill(pygame.Color('black'))
            fire_time += 1
    pygame.quit()


if __name__ == '__main__':
    main_menu()
