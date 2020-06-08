import pygame
import unittest
import random
from snake.constant import *
from snake.game_object import Snake, Food, Wall
from snake.gui import Game
from snake.constant import *


class TestGame(unittest.TestCase):
    def setUp(self):
        self.test_snake = Snake(GREEN, 100, 50)
        self.test_food = Food(BROWN, FOOD_POS_X, FOOD_POS_Y)
        self.test_game = Wall(WALL_POS_X, WALL_POS_Y)
        self.test_level = Game()

    def test_score(self):
        for i in range(0,5):
            self.test_level.score+=1
        self.assertEqual(5, self.test_level.score)

    def test_check_fps(self):
        self.test_level.fps_controller
        self.assertEqual(type(self.test_level.fps_controller), type(pygame.time.Clock()))

    def test_check_error(self):
        test_open = self.test_level.init_and_check_for_errors()
        self.assertEqual(test_open, 'Ok')

    def test_init_display(self):
        test_disp = self.test_level.set_surface_and_title()
        self.assertEqual(test_disp, pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)))




