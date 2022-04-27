# coding: utf-8
# 创建设置类，可以将所有设置放在这个文件里面便于管理
class Setting():
	"""存储《外星人入侵》的所有设置的类"""

	def __init__(self):
		# 屏幕设置
		self.screen_width = 1200
		self.screen_height = 800
		# 设置背景颜色,RGB(230,230,230)表示灰色颜色
		self.bgcolor = (230,230,230)

		# 子弹设置

		# 子弹形状大小
		self.bullet_width = 3
		"""初始化游戏的静态设置"""
		self.bullet_height = 15
		# 子弹颜色
		self.bullet_color = (60,60,60)
		# 控制子弹的数目
		self.bullets_allowed = 3

		# 设置外星人舰队下移速度
		self.fleet_drop_speed = 15

		# 设置飞船生命的数目
		self.ship_limit = 3
		# 以多大的速度加快游戏节奏
		self.speedup_scale = 1.1
		# 游戏节奏加快之后，外星人的点数也应该提高相应的分数
		self.score_scale = 1.5
		# 调用动态设置函数来设置移动速度相关变量
		self.initialize_dynamic_settings()


	def initialize_dynamic_settings(self):
		"""初始化开始游戏,并且随着游戏进行而变化的设置"""
		# 设置飞船的运动速度
		self.ship_speed_factor = 1.5
		# 子弹速度
		self.bullet_speed_factor = 3
		# 设置外星人移动的速度
		self.alien_speed_factor = 1
		# fleet_direction 为1时表示右移，为-1时表示左移
		self.fleet_direction = 1
		# 计分
		self.alien_point = 50

	def increase_speed(self):
		"""提高速度设置"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_point *= self.score_scale
