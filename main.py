import pygame
from snake.game_process.control import Control
from snake.game_object.snake import Snake
from gui.gui import Gui
from snake.game_object.food import Food

pygame.init()

window = pygame.display.set_mode((440, 440))
pygame.display.set_caption("Snake")
control = Control()
snake = Snake()
gui = Gui()
food = Food()

gui.init_field()
food.get_food_position(gui)
food.get_yellow_food_position(gui)
food.get_blue_food_position(gui)
var_speed = 0

while control.flag_game:
    gui.check_win_lose()
    control.control()
    window.fill(pygame.Color("black"))

    if gui.game == "GAME":
        snake.draw_snake(window)
        food.draw_food(window)
        food.draw_yellow_food(window)
        food.draw_blue_food(window)
    elif gui.game == "WIN":
        gui.draw_win(window)
    elif gui.game == "LOSE":
        gui.draw_lose(window)

    gui.draw_indicator(window)
    gui.draw_level(window)
    # gui.draw_level_two(window)

    if var_speed % 10 == 0 and gui.game == "GAME":
        snake.moove(control)
        snake.check_barriers(gui)
        snake.eat(food, gui)
        snake.check_end_window()
        snake.animation()
    var_speed += 1
    pygame.display.flip()
