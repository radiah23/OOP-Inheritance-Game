import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from my_sprite import my_sprite

class colliding_object(my_sprite):
    def __init__(self, image_fname, loc=(0, 0)):
        super().__init__(image_fname, loc)
        locx, locy = loc
        self.bounding_box = pygame.Rect(locx, locy, self.get_width(), self.get_height())
    
    def get_bounding_box(self):
        return self.bounding_box
    
    def is_colliding_with(self, colliding_object):
        if self.get_bounding_box().colliderect(colliding_object.get_bounding_box()):
            return True
        else:
            return False
    def __str__(self):
        print(f"Vehicle{self.}")




