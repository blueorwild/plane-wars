import os, pygame, threading
import handle_events as he
import draw_game as dg
import sets, player, enemy, options

def enemies_active(bg_rect, player_object, enemies, enemies_bullets):
    t1 = threading.Thread(target=enemy.add_enemy, args=(bg_rect, enemies)) # 添加敌人 
    t2 = threading.Thread(target=enemy.fire, args=(player_object, enemies, enemies_bullets)) # 敌人开火
    t1.start()
    t2.start()
    return

def run_game():
    # 初始化游戏并创建游戏元素
    pygame.init()
    # 真正加载字体必须在pygame.init()之后
    sets.score_font = pygame.font.Font(sets.score_font, sets.score_font_size)
    bg = pygame.display.set_mode((sets.bg_width, sets.bg_height))
    bg_rect = bg.get_rect()
    pygame.display.set_caption("打灰机")

    option = options.Options(bg_rect)
    player_object = player.Player(bg_rect)
    enemies = []
    player_bullets = []
    enemies_bullets = []
    
    # 开始游戏
    sets.status = 'INIT'
    enemies_active(bg_rect, player_object, enemies, enemies_bullets)
    while True:
        dg.draw_main(bg, player_object, enemies, player_bullets, enemies_bullets, option)
        he.check_events(player_object, player_bullets, option)
        if sets.status == 'RUNNING':
            player_object.move()
            enemy.update_enemies(enemies)
            player.update_bullets(bg_rect, player_bullets)
            enemy.update_bullets(bg_rect, enemies_bullets)
            player_object.hit_enemy(enemies, player_bullets)
            enemy.hit_player(player_object, enemies_bullets)
        elif sets.status == 'END':
            pygame.mouse.set_visible(True)
            player_object.hp = sets.player_hp
            player_object.score = 0
            enemies.clear()
            player_bullets.clear()
            enemies_bullets.clear()
            sets.status = 'INIT'
        elif sets.status == 'EXIT': os._exit(0)
        
        
    return
        
run_game()
