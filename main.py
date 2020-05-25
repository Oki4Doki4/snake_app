import pygame
from control import Control
from snake import Snake
from gui import Gui
from food import Food


pygame.init()

window = pygame.display.set_mode((441,441))
pygame.display.set_caption("Snake")
control = Control()
snake = Snake()
gui = Gui()
food = Food()

gui.init_field()
food.get_food_position(gui)
var_speed = 0


while control.flag_game:
    control.control()
    window.fill(pygame.Color("black"))
    snake.draw_snake(window)
    food.draw_food(window)
    gui.draw_level(window)
    if var_speed % 10 == 0:
        snake.moove(control)
        snake.eat(food, gui)
        snake.check_end_window()
        snake.animation()
    var_speed += 1
    pygame.display.flip()


