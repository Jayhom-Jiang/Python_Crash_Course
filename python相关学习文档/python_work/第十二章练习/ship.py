# coding: utf-8
import pygame

class Ship():
	"""定义一个飞船的类对飞船的位置等进行定义设置"""

	def __init__(self,ai_settings,screen):
		"""初始化飞船并设置其初始位置"""
		# 将主屏从alien_invasion.py文件传过来为了设置图像在屏幕（已获取外接矩形也就是screen的rect对象）的位置
		self.screen=screen
		# 将alien_invasion.py中关于Setting的对象传递过来
		self.ai_settings=ai_settings

		# 加载飞船图像并获取其外接矩形(rect对象)
		# image就是图像的surface就如同alien_invasion.py中的screen一样
		self.image = pygame.image.load("images/ship.bmp")
		# 使用get_rect()获取相应surface的属性rect
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()

		# 将每艘飞船放置在屏幕底部中央,也就是将图像的rect对象放在screen的rect对象，也就是被赋值
		# centerx把屏幕的中心点先赋值给元素的中心点，bottom然后再把屏幕的底部赋值给元素的底部，效果就是让元素位于屏幕的底部中心的位置
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# 在飞船的属性center中存储小数值
		self.center=float(self.rect.centerx)

		# 移动左右标志位
		self.moving_right=False
		self.moving_left=False

	    # 更新飞船对的位置

	def blitme(self):
		"""在屏幕上指定位置上描绘飞船"""
		# 在screen这个surface上描绘图像这个surface用函数：blit(需要描绘的图像surface,图像的外接矩形的位置)
		self.screen.blit(self.image,self.rect)
	def update(self):
		"""更新飞船在屏幕中的位置"""
		# 因为rect不能存储小数值，但是设置的飞船速度可以是有小数值的数，所以现在更新的是可以存放小数值的变量center
		# 限制飞船的活动范围，让飞船只能在生成的游戏屏幕之内运动(self.rect.right表示飞船的外接矩形的x坐标,self.screen_rect.right表示屏幕最右端的x坐标,屏幕最左端的x坐标就是0 )
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center+=self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center-=self.ai_settings.ship_speed_factor

		# 再根据最新的center的值更新rect对象，因为最终还是要在surface上进行显示，所以需要更新赋值，即使只保留了center的整数部分但不会影响太大感受
		self.rect.centerx=self.center

