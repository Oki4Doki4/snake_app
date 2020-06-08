import pygame
from gui.screen import Game
from snake.game_object.snake import Snake
from snake.game_object.food import Food
from snake.game_object.wall import Wall

gui = Game()
snake = Snake(gui.green)
wall = Wall()

food = Food(gui.brown, gui.screen_width, gui.screen_height)

gui.init_and_check_for_errors()
gui.set_surface_and_title()
wall_list = wall.create_level(wall.load_wall("level_one.txt"))

while True:
    snake.change_to = gui.event_loop(snake.change_to)
    snake.validate_direction_and_change()
    snake.change_head_position()

    gui.score, food.food_pos, food.food_yellow_pos = snake.snake_body_mechanism(
        gui.score, food.food_pos, food.food_yellow_pos, gui.screen_width, gui.screen_height)

    snake.draw_snake(gui.play_surface, gui.white)

    gui.draw_level(gui.load_level("level_one.txt"))

    food.draw_food(gui.play_surface)
    food.draw_yellow_food(gui.play_surface)

    snake.check_for_boundaries(
        gui.game_over, gui.screen_width, gui.screen_height, wall_list)

    gui.show_score()
    gui.refresh_screen()
