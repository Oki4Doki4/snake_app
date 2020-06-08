import pygame
import unittest
import random
from snake.constant import *
from snake.game_object import Snake, Food, Wall


class Test(unittest.TestCase):
    def setUp(self):
        self.test_snake = Snake(GREEN, 100, 50)
        self.test_food = Food(BROWN, FOOD_POS_X, FOOD_POS_Y)

    def test_init_snake(self):
        test_game_object = Snake(GREEN, 100, 50)
        self.assertTrue(isinstance(test_game_object, Snake))

    def test_init_food(self):
        test_food = Food(BLACK, FOOD_POS_X, FOOD_POS_Y)
        self.assertTrue(isinstance(test_food, Food))

    def test_block_init(self):
        test_wall = Wall(WALL_POS_Y, WALL_POS_X)
        self.assertTrue(isinstance(test_wall, Wall))

    def test_initialisation_body(self):
        test_snake_body = [[100, 50], [90, 50], [80, 50]]
        self.assertEqual(test_snake_body, self.test_snake.snake_body)

    def test_initialisation_head(self):
        test_snake_head = [100, 50]
        self.assertEqual(test_snake_head, self.test_snake.snake_head_pos)

    def test_animation_snake(self):
        body = [[100, 50], [90, 50], [80, 50]]
        head = [100, 50]
        default_snake = body.insert(0, list(head))
        self.assertEqual(self.test_snake.snake_body.insert(0, list(head)), default_snake)
