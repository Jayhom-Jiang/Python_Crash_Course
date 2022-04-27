# coding: utf-8
import pygame
# 从pygame中引入Sprite类(精灵类),可以将游戏中相关元素编组，进而同时操作编组中的所有元素
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""一个对飞船发射的子弹进行管理的类"""

	def __init__(self,ai_settings,screen,ship):
		"""在飞船所处的位置创建一个子弹对象"""
		super().__init__()
		# 这里赋值定义的screen是供draw_bullet(self)函数使用，进行在屏幕上绘制子弹
		self.screen=screen

		# 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置: pygame.Rect(left, top, width, height)
		self.rect = pygame.Rect(0,0,ai_settings.bullet_width,
		ai_settings.bullet_height)
		# centerx把飞船的中心点先赋值给元素的中心点，top然后再把飞船的底部赋值给元素的底部，效果就是让子弹位于飞船的移动前的位置
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		#存储用小数(变量y)表示的子弹位置纵轴y
		self.y = float(self.rect.y)

		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor

	def update(self):
		"""向上移动子弹"""
		# 屏幕左上角是(0,0)所以当子弹往上移动时这意味着y坐标会不断变小
		self.y -= self.speed_factor

		# 更新表示子弹的rect位置
		self.rect.y = self.y

	def draw_bullet(self):
		"""在屏幕上绘制子弹"""
		# self.rect就是传递子弹在screen中的位置
		pygame.draw.rect(self.screen,self.color,self.rect)






