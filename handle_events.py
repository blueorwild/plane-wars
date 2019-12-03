import sys, pygame
import sets

def handle_key_down(key, player_object, player_bullets):
    if key == pygame.K_RIGHT:
        player_object.is_move = True
        player_object.move_direct = 'RIGHT'
    elif key == pygame.K_LEFT:
        player_object.is_move = True
        player_object.move_direct = 'LEFT'
    elif key == pygame.K_UP:
        player_object.is_move = True
        player_object.move_direct = 'UP'
    elif key == pygame.K_DOWN:
        player_object.is_move = True
        player_object.move_direct = 'DOWN'
    elif key == pygame.K_SPACE:
        player_object.fire(player_bullets)
    return     

def handle_key_up(key, player_object):
    if key in (pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN): 
        player_object.is_move = False
    return

def handle_mouse_down(option, point):
    if sets.status == 'INIT':  
        if option.start_button_rect.collidepoint(point):
            sets.status = 'START'
    return

def handle_mouse_up(option, point):
    if sets.status == 'START':
        if option.start_button_rect.collidepoint(point):
            sets.status = 'RUNNING'
            pygame.mouse.set_visible(False)  # 游戏运行时隐藏光标
        else: sets.status = 'INIT'
    return

def check_events(player_object, player_bullets, option):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sets.status = 'EXIT'
        elif event.type == pygame.KEYDOWN:
            handle_key_down(event.key, player_object, player_bullets)
        elif event.type == pygame.KEYUP:
            handle_key_up(event.key, player_object)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            point = pygame.mouse.get_pos()
            handle_mouse_down(option, point)
        elif event.type == pygame.MOUSEBUTTONUP:
            point = pygame.mouse.get_pos()
            handle_mouse_up(option, point)
    return