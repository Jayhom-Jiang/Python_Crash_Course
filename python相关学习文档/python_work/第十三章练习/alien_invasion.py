# coding: utf-8

from setting import Setting

import pygame

from ship import Ship

import game_function as gf

from pygame.sprite import Group

from alien import Alien

from game_stats import GameStats

from button import Button

from scoreboard import Scoreboard

def run_game():
	# 初始化游戏并创建一个屏幕对象screen
	pygame.init()
	# 制定游戏窗口的尺寸,通过设置类的对象来引用变量
	ai_settings=Setting()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# 创建Play按钮
	play_button = Button(ai_settings,screen,"Play")

	# 创建一个用于存储游戏统计信息的实例
	stats = GameStats(ai_settings)

	# 创建存储游戏的统计实例，并创建记分牌
	sb = Scoreboard(ai_settings,screen,stats)

	# 创建一艘飞船对象
	ship = Ship(ai_settings,screen)

	# 创建一个用于存储子弹的编组
	bullets = Group()

	# 创建一个外星人
	aliens = Group()

	# 因为在游戏开始时就需要创建显示外星人舰队
	gf.create_fleet(ai_settings,screen,ship,aliens)

	#开始游戏的循环
	while True:


		# 监视键盘和鼠标事件
		gf.check_events(ai_settings,screen,ship,bullets,play_button,stats,aliens,sb)

		if stats.game_active:

			# 更新飞船的位置
			ship.update()

			# 更新子弹的位置
			# 删除已经消失的子弹
			# 删除互相碰撞的子弹和外星人
			gf.update_bullets(ai_settings,screen,ship,aliens,bullets,stats,sb)

			# 更新外星人的位置，一定要放在子弹更新位置之后，因为这样方便判断子弹是否打中了外星人
			gf.update_aliens(ai_settings,ship,aliens,stats,screen,bullets,sb)
		# 每次循环时都重新绘制屏幕
		# 调用Ship类方法将飞船对象描绘在屏幕
		# 让最近绘制的屏幕可见
		gf.update_screen(ai_settings,screen,ship,aliens,bullets,play_button,stats,sb)


# 启动游戏开始
run_game()

