# 敌人飞机的相关东西
import pygame,random
from time import sleep
from bullet import Bullet
import sets

class Enemy():
    def __init__(self, bg_rect):
        # 基本配置
        self.bg_rect = bg_rect
        self.plane_image = pygame.image.load(sets.enemy_plane_image)
        self.plane_rect = self.plane_image.get_rect()
        self.plane_speed_x = random.randint \
            (sets.enemy_plane_speed_x[0],sets.enemy_plane_speed_x[1])/ 100
        self.plane_speed_y = random.randint \
            (sets.enemy_plane_speed_y[0],sets.enemy_plane_speed_y[1])/ 100

        # 位置相关（初始背景顶部随机位置）
        self.plane_rect.centerx = random.randint(bg_rect.left, bg_rect.right)
        self.plane_rect.bottom = bg_rect.top
        # 为了更精确的移动 
        self.plane_rect_centerx = float(self.plane_rect.centerx)
        self.plane_rect_centery = float(self.plane_rect.centery)
        return

    def move(self):
        self.plane_rect_centerx += self.plane_speed_x
        self.plane_rect_centery += self.plane_speed_y
        self.plane_rect.centerx = int(self.plane_rect_centerx)
        self.plane_rect.centery = int(self.plane_rect_centery)

# 添加一个敌人
def add_enemy(bg_rect, enemies):
    while True:
        sleep(random.uniform(0, sets.enemy_generate_freq * 2))
        if sets.status != 'RUNNING': continue     
        if len(enemies) < sets.enemy_maximum: # 最多同时出现10个敌人
            new_enemy = Enemy(bg_rect)
            enemies.append(new_enemy)
    return

# 敌人开火（所有敌人创建一新子弹）
def fire(player, enemies, enemies_bullets):
    bullet_image = pygame.image.load(sets.enemy_bullet_image)
    while True:
        sleep(sets.enemy_fire_interval)
        if sets.status != 'RUNNING': continue
        for enemy in enemies:
            # 利用勾股定理计算敌人子弹的移动速度（追踪玩家）
            leg_x = player.plane_rect.centerx - enemy.plane_rect.centerx   # 直角边1
            leg_y = player.plane_rect.centery - enemy.plane_rect.centery   # 直角边2
            hypotenuse = pow(pow(leg_x, 2) + pow(leg_y, 2), 0.5) # 斜边
            speed_x = sets.enemy_bullet_speed * leg_x / hypotenuse
            speed_y = sets.enemy_bullet_speed * leg_y / hypotenuse

            bullet_rect = bullet_image.get_rect()
            bullet_rect.center = enemy.plane_rect.center
            new_bullet = Bullet(bullet_image, bullet_rect, speed_x, speed_y)
            enemies_bullets.append(new_bullet)
    return

# 敌人命中玩家
def hit_player(player, enemies_bullets):
    for bullet in enemies_bullets:
        if player.plane_rect.collidepoint(bullet.rect.center):
            enemies_bullets.remove(bullet)
            player.hp -= 1
            if player.hp == 0:
                sets.status = 'END'
    return

# 刷新敌人并删掉超出范围的敌人
def update_enemies(enemies):
    if len(enemies) > 0:
        bg_rect = enemies[0].bg_rect
        for enemy in enemies:
            enemy.move()
            if enemy.plane_rect.right < bg_rect.left or enemy.plane_rect.left > bg_rect.right \
                or enemy.plane_rect.top > bg_rect.bottom or enemy.plane_rect.bottom < bg_rect.top:
                enemies.remove(enemy)
    return

# 刷新子弹并删除超出范围的子弹
def update_bullets(bg_rect, enemies_bullets):
    for bullet in enemies_bullets:
        bullet.move()
        if not bg_rect.collidepoint(bullet.rect.center):
            enemies_bullets.remove(bullet)
    return