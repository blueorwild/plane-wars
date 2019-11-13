import pygame
import sets
from bullet import Bullet

class Player():
    def __init__(self, bg_rect):
        # 基本配置
        self.bg_rect = bg_rect
        self.plane_image = pygame.image.load(sets.player_plane_image)
        self.plane_rect = self.plane_image.get_rect()
        self.plane_speed = sets.player_plane_speed
        self.hp_image = pygame.image.load(sets.player_hp_image)
        self.hp = sets.player_hp
        self.score = 0
        self.bullet_image = pygame.image.load(sets.player_bullet_image)
        self.bullet_speed = sets.player_bullet_speed

        # 位置相关（初始在背景中央底部）
        self.plane_rect.centerx = bg_rect.centerx
        self.plane_rect.bottom = bg_rect.bottom
        # 为了精确移动
        self.plane_rect_centerx = float(self.plane_rect.centerx)
        self.plane_rect_centery = float(self.plane_rect.centery)
        self.is_move = False
        self.move_direct = 'NULL'
        return

    # 移动
    def move(self):
        if self.is_move:
            if self.move_direct == 'RIGHT' and self.plane_rect.right < self.bg_rect.right: 
                self.plane_rect_centerx += self.plane_speed
            elif self.move_direct == 'LEFT'and self.plane_rect.left > self.bg_rect.left: 
                self.plane_rect_centerx -= self.plane_speed
            elif self.move_direct == 'UP'and self.plane_rect.top > self.bg_rect.top:   
                self.plane_rect_centery -= self.plane_speed
            elif self.move_direct == 'DOWN'and self.plane_rect.bottom < self.bg_rect.bottom: 
                self.plane_rect_centery += self.plane_speed
            self.plane_rect.centerx = int(self.plane_rect_centerx)
            self.plane_rect.centery = int(self.plane_rect_centery)
        return

    # 添加一个新子弹
    def fire(self, player_bullets):
        bullet_rect = self.bullet_image.get_rect()
        bullet_rect.center = self.plane_rect.center
        new_bullet = Bullet(self.bullet_image, bullet_rect, 0, -self.bullet_speed)
        player_bullets.append(new_bullet)
        return

    # 玩家命中敌人
    def hit_enemy(self, enemies, player_bullets):
        for bullet in player_bullets:
            for enemy in enemies:
                if enemy.plane_rect.collidepoint(bullet.rect.center):
                    player_bullets.remove(bullet)
                    enemies.remove(enemy)
                    self.score += 1
        return

# 刷新子弹并删除超出范围的子弹
def update_bullets(bg_rect, player_bullets):
    for bullet in player_bullets:
        bullet.move()
        if not bg_rect.collidepoint(bullet.rect.center):
            player_bullets.remove(bullet)
    return