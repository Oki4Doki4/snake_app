import pygame
import unittest
import random
from snake.game_process.control import Control
from snake.game_object.snake import Snake
from gui.gui import Gui
from snake.game_object.food import Food


class Test(unittest.TestCase):
    def setUp(self):
        self.test_snake = Snake()
        self.test_food = Food()
        self.test_gui = Gui()

    def test_initialisation_body(self):
        test_snake_body = [[45, 45], [34, 45], [23, 45]]
        self.assertEqual(test_snake_body, self.test_snake.body)

    def test_initialisation_head(self):
        test_snake_head = [45, 45]
        self.assertEqual(test_snake_head, self.test_snake.head)

    def test_animation_snake(self):
        self.body = [[45, 45], [34, 45], [23, 45]]
        self.head = [45, 45]
        default_snake = self.body.insert(0, list(self.head))
        self.assertEqual(self.test_snake.animation(), default_snake)

    def test_default_indicator(self):
        test_indicator = self.test_gui.indicator
        self.assertEqual(test_indicator, [[12, 12]])

    def test_append_indicator(self):
        test_indicator = self.test_gui.indicator.append([self.test_gui.indicator[-1][0] + 11, 12])
        default_indicator = [[12, 12]]
        self.assertEqual(test_indicator, [[12, 12]].append([default_indicator[-1][0] + 11, 12]))

    def test_length_indicator(self):
        test_indicator = self.test_gui.indicator
        test_indicator.pop()
        self.assertEqual(len(test_indicator), 0)
