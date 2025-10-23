import my_sprite
from colliding_object import colliding_object
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

class moving_vehicle(colliding_object):
    def __init__(self, image_fname, loc=(0, 0)):
        super().__init__(image_fname, loc)
    
    def set_location(self, loc):
        self.loc = loc
        locx, locy = loc
        self.bounding_box.topleft = (locx, locy)

  