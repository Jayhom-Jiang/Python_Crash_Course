# coding: utf-8
import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
	"""显示得分的信息类"""
	def __init__(self,ai_settings,screen,stats):
		"""初始化显示得分涉及的属性"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats

		# 显示得分信息时显示的字体设置
		self.text_color = (30,30,30)
		# 设置字体
		self.font = pygame.font.SysFont("arial",48)

		# 初始化得分图像
		# 准备包含当前得分和最高分的图像
		self.prep_score()
		self.prep_high_score()
		# 显示等级
		self.prep_level()
		# 显示飞船生命值个数
		self.prep_ships()

	def prep_score(self):
		"""将当前得分转换为一幅渲染的图像"""
		score_str = str(self.stats.score)
		# 函数round通常让小数精确到小数点后几位，小数的位数由第二个参数决定，若为-1则将圆整到最近的10，100，1000等整数倍
		round_score = int(round(self.stats.score,-1))
		# 使用字符串格式设置指令，将数值转换为字符串时插入“，”
		score_str = "{:,}".format(round_score)


		self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bgcolor)

		# 将得分放在屏幕右上角
		self.score_rect = self.score_image.get_rect()
		# 将屏幕右边缘与屏幕右边缘相距20像素
		self.score_rect.right = self.screen_rect.right - 20
		# 将屏幕上边缘与屏幕上边缘相距20像素
		self.screen_rect.top = 20

	def prep_high_score(self):
		"""将最高得分转换为一幅渲染的图像"""
		# 函数round通常让小数精确到小数点后几位，小数的位数由第二个参数决定，若为-1则将圆整到最近的10，100，1000等整数倍
		high_score = int(round(self.stats.high_score,-1))
		# 使用字符串格式设置指令，将数值转换为字符串时插入“，”
		high_score_str = "{:,}".format(high_score)

		self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.ai_settings.bgcolor)

		# 将最高分放在屏幕顶中央
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.high_score_rect.top

	def prep_level(self):
		"""将游戏进行等级转换为一幅渲染的图像"""
		self.level_image = self.font.render(str(self.stats.level),True,self.text_color,self.ai_settings.bgcolor)

		# 将等级放在得分下方
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10

	def prep_ships(self):
		"""显示还剩多少艘飞船"""
		# 创建Ship类的空编组
		self.ships = Group()
		for ship_number in range(self.stats.ship_left):
			ship = Ship(self.ai_settings,self.screen)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)


	def show_score(self):
		"""在屏幕上显示得分等因素"""
		# 绘制飞船
		self.ships.draw(self.screen)
		# 将当前得分图像显示到屏幕上去放在rect的位置
		self.screen.blit(self.score_image,self.score_rect)
		# 将最高得分图像显示到屏幕上去放在rect的位置
		self.screen.blit(self.high_score_image,self.high_score_rect)
		# 将游戏等级图像显示到屏幕上去放在rect的位置
		self.screen.blit(self.level_image,self.level_rect)

