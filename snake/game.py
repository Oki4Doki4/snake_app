import pygame
from snake.gui import Game
from snake.game_object import Snake, Food, Wall
from snake.constant import *

gui = Game()
snake = Snake(gui.green, SNAKE_HEAD_POS_X, SNAKE_HEAD_POS_Y)
wall = Wall(WALL_POS_X, WALL_POS_Y)
food = Food(gui.brown, FOOD_POS_X, FOOD_POS_Y)

gui.init_and_check_for_errors()
gui.set_surface_and_title()
wall_list = wall.create_level(wall.load_wall("level_one.txt"))

while True:
    snake.change_to = gui.event_loop(snake.change_to)
    snake.validate_direction_and_change()
    snake.change_head_position()

    gui.score, food.food_pos, food.food_yellow_pos = snake.snake_body_mechanism(
        gui.score, food.food_pos, food.food_yellow_pos, SCREEN_WIDTH, SCREEN_HEIGHT)

    snake.draw_snake(gui.play_surface, gui.white)

    gui.draw_level(gui.load_level("level_one.txt"))

    food.draw_food(gui.play_surface)
    food.draw_yellow_food(gui.play_surface)

    snake.check_for_boundaries(
        gui.game_over, SCREEN_WIDTH, SCREEN_HEIGHT, wall_list)

    gui.show_score()
    gui.refresh_screen()
