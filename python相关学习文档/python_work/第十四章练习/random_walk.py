# coding: utf-8
# 随机漫步，完全随机
from random import choice

class RandomWalk():
	"""一个生成随机漫步数据的类"""
	# num_points的值设置是需要满足数据足够大也同时能够快速出结果
	def __init__(self,num_points):
		"""初始化随机漫步的属性"""
		self.num_points = num_points

		# 所有随机漫步都始于(0,0)
		self.x_values = [0]
		self.y_values = [0]

	def fill_work(self):
		"""计算随机漫步包含的所有点"""

		# 不断漫步直到列表达到指定长度
		while len(self.x_values) < self.num_points:

			# 决定随机漫步的方向以及沿这个方向前进的距离
			# 若x_direction选择了-1，那么在x轴向左走，如果是1，在x轴向右走
			x_direction = choice([1,-1])
			# x_distance选择一个移动的距离，若选择为0，则不会在x轴上移动
			x_distance = choice([0,1,2,3,4])
			# x_step表示x轴移动的距离
			x_step = x_distance * x_distance

			y_direction = choice([1,-1])
			y_distance = choice([0,1,2,3,4])
			y_step = y_distance * y_distance

			# 拒绝原地踏步，也就是xy轴都没有移动
			if x_step == 0 and y_step == 0:
				continue

			# 计算下一个点的x和y值,用列表中的-1位置表示倒数第一个值，所以下一个点就是每次更新的最后一个点也就是-1
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step

			# 将更新的值加入到列表中从而更新列表倒数第一个值也就是列表中的-1位置
			self.x_values.append(next_x)
			self.y_values.append(next_y)
