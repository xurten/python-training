# Snake game refactored from https://www.youtube.com/watch?v=CD4qAhfFuLo&t=31s
import random
import pygame
from snake_game.cube import Cube, WHITE_COLOR, GREEN_COLOR
from snake_game.snake import Snake


def draw_grid(w, rows, surface):
    size_between_lines = w // rows

    x = 0
    y = 0
    for line in range(rows):
        x = x + size_between_lines
        y = y + size_between_lines

        pygame.draw.line(surface, WHITE_COLOR, (x, 0), (x, w))
        pygame.draw.line(surface, WHITE_COLOR, (0, y), (w, y))


def redraw_window(surface):
    global rows, width, s, snack
    surface.fill((0, 0, 0))
    s.draw(surface)
    snack.draw(surface)
    draw_grid(width, rows, surface)
    pygame.display.update()


def random_snack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

    return x, y


def main():
    global width, rows, s, snack
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = Snake((255, 0, 0), (10, 10))
    snack = Cube(random_snack(rows, s), color=GREEN_COLOR)
    flag = True
    clock = pygame.time.Clock()
    point = 0
    while flag:
        pygame.time.delay(100)
        clock.tick(10)
        s.move()
        print(s.body[0].pos)
        if s.body[0].pos == snack.pos:
            s.add_cube()
            snack = Cube(random_snack(rows, s), color=(0, 255, 0))
            point = point + 1
            pygame.display.set_caption('Number of points ' + str(point))
        if s.body[0].pos[0] == 19:
            print("right ")

        redraw_window(win)


main()
