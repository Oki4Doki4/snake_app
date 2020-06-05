import pygame
import random


class Food:
    def __init__(self):
        self.correct_list = [23, 34, 45, 56, 67, 78, 89, 100, 111, 122, 133, 144, 155, 166, 177, 188, 199, 210, 221,
                             232, 243, 254, 265, 276, 287, 298, 309, 320, 331, 342, 353, 364, 375, 386, 397, 408]

        self.food_position_x = 1
        self.food_position_y = 1

        self.yellow_food_pos_x = 1
        self.yellow_food_pos_y = 1

        self.blue_food_pos_x = 1
        self.blue_food_pos_y = 1

    def get_food_position(self, gui):
        self.food_position_x = random.choice(self.correct_list)
        self.food_position_y = random.choice(self.correct_list)

    def draw_food(self, window):
        pygame.draw.rect(window, pygame.Color("Red"), pygame.Rect(self.food_position_x, self.food_position_y, 10, 10))

    def get_yellow_food_position(self, gui):
        self.yellow_food_pos_x = random.choice(self.correct_list)
        self.yellow_food_pos_y = random.choice(self.correct_list)

    def draw_yellow_food(self, window):
        pygame.draw.rect(window, pygame.Color("Yellow"),
                         pygame.Rect(self.yellow_food_pos_x, self.yellow_food_pos_y, 10, 10))

    def get_blue_food_position(self, gui):
        self.blue_food_pos_x = random.choice(self.correct_list)
        self.blue_food_pos_y = random.choice(self.correct_list)

    def draw_blue_food(self, window):
        pygame.draw.rect(window, pygame.Color("Blue"), pygame.Rect(self.blue_food_pos_x, self.blue_food_pos_y, 10, 10))
