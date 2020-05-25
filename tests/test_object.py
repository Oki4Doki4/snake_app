import pygame
import unittest
import random
from game_process.control import Control
from game_object.snake import Snake
from gui.gui import Gui
from game_object.food import Food


class Test(unittest.TestCase):
    def setUp(self):
        self.test_snake = Snake()
        self.test_food = Food()


    def test_initialisation_body(self):
        test_snake_body = [[45,45], [34,45], [23,45]]
        self.assertEqual(test_snake_body, self.test_snake.body)

    def test_initialisation_head(self):
        test_snake_head = [45,45]
        self.assertEqual(test_snake_head, self.test_snake.head)