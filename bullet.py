import pygame

class Bullet():
    def __init__(self, image, position_rect, speed_x, speed_y):
        # 基本配置
        self.image = image
        self.rect = position_rect
        self.speed_x = speed_x
        self.speed_y = speed_y

        # 位置相关
        self.rect_centerx = float(self.rect.centerx)
        self.rect_centery = float(self.rect.centery)
        return

    # 移动
    def move(self):
        self.rect_centerx += self.speed_x
        self.rect_centery += self.speed_y
        self.rect.centerx = int(self.rect_centerx)
        self.rect.centery = int(self.rect_centery)
        return

    # 画在屏幕上
    def draw(self, bg):
        bg.blit(self.image, self.rect)
        return




