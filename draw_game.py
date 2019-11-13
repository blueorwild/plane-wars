import pygame
import sets

def draw_player_score(bg, player):
    # 把数字转成字符串再转为图片
    score_str = 'score: ' + str(player.score)
    score_image = sets.score_font.render(score_str, True, sets.score_color)
    score_rect = score_image.get_rect()
    bg_rect = bg.get_rect()
    score_rect.top = bg_rect.top + 20
    score_rect.right = bg_rect.right - 20
    bg.blit(score_image, score_rect)
    return
 
def draw_start_button(bg, option):
    if sets.status == 'INIT':
        bg.blit(option.start_button_up_image, option.start_button_rect)
    elif sets.status == 'START':
        bg.blit(option.start_button_down_image, option.start_button_rect)
    return

def draw_player_hp(bg, player):
    bg_rect = bg.get_rect()
    for i in range(0, player.hp):
        hp_rect = player.hp_image.get_rect()
        hp_rect.top = bg_rect.top + hp_rect.height
        hp_rect.left = hp_rect.width + bg_rect.left + (i << 1) * hp_rect.width
        bg.blit(player.hp_image, hp_rect)
    return

def draw_player_plane(bg, player):
    bg.blit(player.plane_image, player.plane_rect)
    return

def draw_enemies_plane(bg, enemies):
    for enemy in enemies:
        bg.blit(enemy.plane_image, enemy.plane_rect)
    return

def draw_player_bullets(bg, player_bullets):
    for bullet in player_bullets:
        bg.blit(bullet.image, bullet.rect)
    return

def draw_enemies_bullets(bg, enemies_bullets):
    for bullet in enemies_bullets:
        bg.blit(bullet.image, bullet.rect)
    return

def draw_main(bg, player, enemies, player_bullets, enemies_bullets, option):
    bg.fill(sets.bg_color)
    if sets.status != 'RUNNING':
        draw_start_button(bg, option)
    else:
        draw_enemies_bullets(bg, enemies_bullets)
        draw_player_bullets(bg, player_bullets)
        draw_enemies_plane(bg, enemies)
        draw_player_plane(bg, player)
        draw_player_hp(bg, player)
        draw_player_score(bg, player)
    pygame.display.flip()
    return