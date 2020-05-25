import pygame
import random


class Food:
    def __init__(self):

        self.food_position = []
       # self.food_position[0] = 1
       # self.food_position[1] = 1

    def get_food_position(self, gui):
        """Выдает рандомное значение координат еды"""
       # self.food_position = random.choice(gui.field)
        self.food_position = [random.randint(1, 441) ,random.randint(1, 441)]

       # self.food_position[0] = random.randint(6, 10)
       # self.food_position[1] = random.randint(6, 100)

    def draw_food(self, window):
        """отрисовка еды"""
        pygame.draw.rect(window, pygame.Color("red"), pygame.Rect(self.food_position[0], self.food_position[1], 10,10))