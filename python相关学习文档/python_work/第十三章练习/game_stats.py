# coding: utf-8

class GameStats():
	"""跟踪游戏的统计信息"""

	def __init__(self,ai_settings):
		"""初始化统计信息"""
		self.ai_settings = ai_settings
		self.reset_stats()

		# 游戏刚启动时处于非活动状态，只有点击按键play然后可以开始运行游戏
		self.game_active = False

		# 最高分设置，并且不会重置最高分一般情况
		self.high_score = 0

	def reset_stats(self):
		"""初始化在游戏运行期间可能变化的统计信息"""
		self.ship_left = self.ai_settings.ship_limit

		# 为在每次开始的时候才重置分数，所以不能在__init__中设置分数变量
		self.score = 0
		# 设置游戏等级,为在每次开始的时候才重置等级，所以不能在__init__中设置分数变量
		self.level = 1


