import pygame
import sets

class Options():
    def __init__(self, bg_rect):
        self.start_button_up_image = pygame.image.load(sets.start_button_up_image)
        self.start_button_down_image = pygame.image.load(sets.start_button_down_image)
        self.start_button_rect =  self.start_button_up_image.get_rect()
        self.start_button_rect.center = bg_rect.center
        return