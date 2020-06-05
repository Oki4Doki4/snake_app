import pygame


class Snake:
    def __init__(self):
        self.head = [45, 45]
        self.body = [[45, 45], [34, 45], [23, 45]]
        self.score = 0

    def draw_snake(self, window):
        for segment in self.body:
            pygame.draw.rect(window, pygame.Color("green"), pygame.Rect(segment[0], segment[1], 10, 10))

    def moove(self, control):
        if control.flag_direction == "RIGHT":
            self.head[0] += 11
        elif control.flag_direction == "LEFT":
            self.head[0] -= 11
        elif control.flag_direction == "UP":
            self.head[1] -= 11
        elif control.flag_direction == "DOWN":
            self.head[1] += 11

    def animation(self):
        self.body.insert(0, list(self.head))
        self.body.pop()

    def check_end_window(self):
        if self.head[0] == 419:
            self.head[0] = 23
        elif self.head[0] == 12:
            self.head[0] = 419
        elif self.head[1] == 23:
            self.head[1] = 419
        elif self.head[1] == 419:
            self.head[1] = 34

    def eat(self, food, gui):
        if self.head[0] == food.food_position_x and self.head[1] == food.food_position_y:
            self.body.append([food.food_position_x, food.food_position_y])
            gui.get_new_indicator()
            food.get_food_position(gui)
            food.get_blue_food_position(gui)
            food.get_yellow_food_position(gui)

        elif self.head[0] == food.blue_food_pos_x and self.head[1] == food.blue_food_pos_y:
            self.body.append([food.blue_food_pos_x, food.blue_food_pos_y])
            food.get_food_position(gui)
            food.get_blue_food_position(gui)
            gui.get_new_indicator()
            gui.get_new_indicator()

        elif self.head[0] == food.yellow_food_pos_x and self.head[1] == food.yellow_food_pos_y:
            self.body.pop()
            gui.indicator.pop()
            food.get_food_position(gui)
            food.get_blue_food_position(gui)
            food.get_yellow_food_position(gui)

    def check_barriers(self, gui):
        if self.head in gui.barrier:
            self.body.pop()
            gui.indicator.pop()
        if self.head in self.body[1:]:
            self.body.pop()
            gui.indicator.pop()
