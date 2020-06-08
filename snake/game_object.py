import pygame
import sys
import random


class Snake:
    def __init__(self, snake_color, x, y):

        self.snake_head_pos = [x, y]  # [x, y]

        self.snake_body = [[x, y], [x-10, y], [x-20, y]]
        self.snake_color = snake_color

        self.direction = "RIGHT"

        self.change_to = self.direction

    def validate_direction_and_change(self):

        if any((self.change_to == "RIGHT" and not self.direction == "LEFT",
                self.change_to == "LEFT" and not self.direction == "RIGHT",
                self.change_to == "UP" and not self.direction == "DOWN",
                self.change_to == "DOWN" and not self.direction == "UP")):
            self.direction = self.change_to

    def change_head_position(self):

        if self.direction == "RIGHT":
            self.snake_head_pos[0] += 10
        elif self.direction == "LEFT":
            self.snake_head_pos[0] -= 10
        elif self.direction == "UP":
            self.snake_head_pos[1] -= 10
        elif self.direction == "DOWN":
            self.snake_head_pos[1] += 10

    def snake_body_mechanism(
            self, score, food_pos, food_yellow_pos, screen_width, screen_height):

        self.snake_body.insert(0, list(self.snake_head_pos))

        if (self.snake_head_pos[0] == food_pos[0] and
                self.snake_head_pos[1] == food_pos[1]):

            food_pos = [random.randrange(1, screen_width / 10) * 10,
                        random.randrange(1, screen_height / 10) * 10]

            score += 1
        elif self.snake_head_pos[0] == food_yellow_pos[0] and self.snake_head_pos[1] == food_yellow_pos[1]:
            self.snake_body.pop()
            self.snake_body.pop()
            food_yellow_pos = [random.randrange(1, screen_width / 10) * 10,
                               random.randrange(1, screen_height / 10) * 10]
            score -= 1

        else:
            self.snake_body.pop()
        return score, food_pos, food_yellow_pos

    def draw_snake(self, play_surface, surface_color):
        play_surface.fill(surface_color)
        for pos in self.snake_body:
            pygame.draw.rect(
                play_surface, self.snake_color, pygame.Rect(
                    pos[0], pos[1], 10, 10))

    def check_for_boundaries(self, game_over, screen_width, screen_height, wall_list):
        if any((
                self.snake_head_pos[0] > screen_width - 10
                or self.snake_head_pos[0] < 0,
                self.snake_head_pos[1] > screen_height - 10
                or self.snake_head_pos[1] < 0,
                self.snake_head_pos in wall_list
        )):
            game_over()
        for block in self.snake_body[1:]:
            if (block[0] == self.snake_head_pos[0] and
                    block[1] == self.snake_head_pos[1]):
                game_over()


class Food:
    def __init__(self, food_color, x, y):
        self.food_color = food_color
        self.food_size_x = 10
        self.food_size_y = 10
        self.food_pos = [x,y]

        self.food_yellow_pos = [x+20, y+40]

    def draw_food(self, play_surface):
        pygame.draw.rect(play_surface, self.food_color, pygame.Rect(
            self.food_pos[0], self.food_pos[1],
            self.food_size_x, self.food_size_y))

    def draw_yellow_food(self, play_surface):
        pygame.draw.rect(play_surface, pygame.Color("Yellow"), pygame.Rect(
            self.food_yellow_pos[0], self.food_yellow_pos[1],
            self.food_size_x, self.food_size_y))


class Wall:
    def __init__(self, pos_x, pos_y):

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.wall_list = [self.pos_x, self.pos_y]

    def load_wall(self, name):

        fullname = 'levels/' + name
        with open(fullname, 'r') as map_file:
            level_map = []
            for line in map_file:
                line = line.strip()
                level_map.append(line)
        return level_map

    def create_level(self, level_map):
        self.wall_list = []
        self.pos_x = 0
        self.pos_y = 0
        for y in range(len(level_map)):
            for x in range(len(level_map)):
                if level_map[y][x] == "#":
                    self.wall_list.append([self.pos_x, self.pos_y])
                self.pos_x += 20
            self.pos_x = 0
            self.pos_y += 20
        return self.wall_list
