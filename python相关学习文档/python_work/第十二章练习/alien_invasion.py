# coding: utf-8

from setting import Setting

import pygame

from ship import Ship

import game_function as gf

from pygame.sprite import Group

def run_game():
	# 初始化游戏并创建一个屏幕对象screen
	pygame.init()
	# 制定游戏窗口的尺寸,通过设置类的对象来引用变量
	ai_settings=Setting()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# 创建一艘飞船对象
	ship = Ship(ai_settings,screen)

	# 创建一个用于存储子弹的编组
	bullets = Group()

	#开始游戏的循环
	while True:


		# 监视键盘和鼠标事件
		gf.check_events(ai_settings,screen,ship,bullets)

        # 更新飞船的位置
		ship.update()

		# 更新子弹的位置
		# 删除已经消失的子弹
		gf.update_bullets(bullets)

		# 每次循环时都重新绘制屏幕
		# 调用Ship类方法将飞船对象描绘在屏幕
		# 让最近绘制的屏幕可见
		gf.update_screen(ai_settings,screen,ship,bullets)

# 启动游戏开始
run_game()

