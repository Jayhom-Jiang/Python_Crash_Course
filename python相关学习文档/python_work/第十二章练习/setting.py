# coding: utf-8
# 创建设置类，可以将所有设置放在这个文件里面便于管理
class Setting():
	"""存储《外星人入侵》的所有设置的类"""

	def __init__(self):
		"""初始化游戏的设置"""
		# 屏幕设置
		self.screen_width = 1200
		self.screen_height = 800
		# 设置背景颜色,RGB(230,230,230)表示灰色颜色
		self.bgcolor = (230,230,230)
		# 设置飞船的运动速度
		self.ship_speed_factor = 1.5
		# 子弹设置
		# 子弹速度
		self.bullet_speed_factor = 1
		# 子弹形状大小
		self.bullet_width = 3
		self.bullet_height = 15
		# 子弹颜色
		self.bullet_color = (60,60,60)
		# 控制子弹的数目
		self.bullets_allowed = 3
