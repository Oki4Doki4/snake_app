import pygame
import sys
import time
from const.constant import *


class Game:
    def __init__(self):
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT

        self.red = RED
        self.green = GREEN
        self.black = BLACK
        self.white = WHITE
        self.brown = BROWN

        self.fps_controller = pygame.time.Clock()

        self.score = SCORE

    def init_and_check_for_errors(self):
        check_errors = pygame.init()
        if check_errors[1] > 0:
            sys.exit()
        else:
            print('Ok')

    def set_surface_and_title(self):
        self.play_surface = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Snake Game')

    def event_loop(self, change_to):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = "RIGHT"
                elif event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = "LEFT"
                elif event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = "UP"
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = "DOWN"
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        return change_to

    def refresh_screen(self):
        """обновляем экран и задаем фпс"""
        pygame.display.flip()
        Game().fps_controller.tick(23)

    def show_score(self, choice=1):
        s_font = pygame.font.SysFont('monaco', 24)
        s_surf = s_font.render(
            'Score: {0}'.format(self.score), True, self.black)
        s_rect = s_surf.get_rect()
        if choice == 1:
            s_rect.midtop = (80, 10)
        else:
            s_rect.midtop = (360, 120)
        self.play_surface.blit(s_surf, s_rect)

    def game_over(self):
        go_font = pygame.font.SysFont('monaco', 72)
        go_surf = go_font.render('Game over', True, self.red)
        go_rect = go_surf.get_rect()
        go_rect.midtop = (200, 15)
        self.play_surface.blit(go_surf, go_rect)
        self.show_score(0)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()

    def load_level(self, name):

        fullname = 'levels/' + name
        with open(fullname, 'r') as map_file:
            level_map = []
            for line in map_file:
                line = line.strip()
                level_map.append(line)
        return level_map

    def draw_level(self, level_map):
        game_map = []
        pos_x = 0
        pos_y = 0
        for y in range(len(level_map)):
            for x in range(len(level_map)):
                if level_map[y][x] == "#":
                    game_map.append(pygame.draw.rect(self.play_surface,
                                                     pygame.Color("grey"), pygame.Rect(pos_x, pos_y, 10, 10)))
                pos_x += 20
            pos_x = 0
            pos_y += 20
        return game_map
