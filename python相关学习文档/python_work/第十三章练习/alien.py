# coding: utf-8
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""表示单个外星人的类"""
	def __init__(self,ai_settings,screen):
		"""初始化外星人并设置其初始位置"""
		super().__init__()
		# 这里赋值定义的screen是为了下面的blitme(self)函数服务
		self.screen = screen
		self.ai_settings = ai_settings

		# 加载外星人图像，并设置rect属性
		self.image = pygame.image.load("images/alien.bmp")
		self.rect = self.image.get_rect()

		# 每个外星人最初都在屏幕左上角附近,直接将矢量图的宽度width和高度height直接作为矢量图在屏幕x和y轴的位置
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# 存储外星人的准确x轴位置
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
	def update(self):
		"""向左或者右移动外星人"""
		self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
		# 再用移动变化之后的数据更新rect对象
		self.rect.x = self.x

	def check_edges(self):
		"""如果外星人位于屏幕边缘，就返回True"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left < 0:
			return True

	def blitme(self):
		"""在指定位置绘制外星人"""
		self.screen.blit(self.image,self.rect)




