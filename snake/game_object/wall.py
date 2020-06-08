import pygame
import sys
import time
from const.constant import *


class Wall:
    def __init__(self):

        self.pos_x = 0
        self.pos_y = 0
        self.wall_list = [self.pos_x, self.pos_y]

    def load_wall(self, name):

        fullname = 'levels/' + name
        with open(fullname, 'r') as map_file:
            level_map = []
            for line in map_file:
                line = line.strip()
                level_map.append(line)
        return level_map

    def create_level(self, level_map):
        self.wall_list = []
        self.pos_x = 0
        self.pos_y = 0
        for y in range(len(level_map)):
            for x in range(len(level_map)):
                if level_map[y][x] == "#":
                    self.wall_list.append([self.pos_x, self.pos_y])
                self.pos_x += 20
            self.pos_x = 0
            self.pos_y += 20
        return self.wall_list
