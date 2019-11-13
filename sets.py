# 打飞机的游戏基本设置

# 屏幕
bg_width = 1200
bg_height = 800
bg_color = (10, 10, 10)

# 飞机
player_plane_image = 'images/player_plane.png'
enemy_plane_image = 'images/enemy_plane.png'
player_plane_speed = 1.0
enemy_plane_speed_x = (-10, 10)  # 随机值范围，需要除以100
enemy_plane_speed_y = (20, 30)  # 随机值范围，需要除以100

# 子弹
player_bullet_image = 'images/player_bullet.png'
enemy_bullet_image = 'images/enemy_bullet.png'
player_bullet_speed = 1.5
enemy_bullet_speed = 0.5

# 血量
player_hp_image = 'images/player_hp.png'
player_hp = 5

# 分数
score_color = (250, 250, 0)
score_font = 'images/Inkfree.ttf'
score_font_size = 32

# 菜单
start_button_up_image = 'images/start_button_up.png'
start_button_down_image = 'images/start_button_down.png'

# 其它 
enemy_maximum = 10         # 同时出现在屏幕上的敌人最大数量
enemy_generate_freq = 0.5  # 平均多少秒生成一个敌人
enemy_fire_interval = 3    # 敌人多少秒开火一次
status = 'INIT' # INIT/START/RUNNING/END/EXIT

        