# coding: utf-8
import matplotlib.pyplot as plt

from random_walk import RandomWalk
# 模拟多次随机漫步
while True:

	# 创建一个RandomWalk实例，调用类方法产生随机漫步的点
	rw = RandomWalk(10000)

	# 调用方法
	rw.fill_work()

	# 绘制rw对象的随机漫步产生的点,并且给点着色
	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,s=15)

	# 突出起点和终点
	plt.scatter(0,0,c='green',s=100)
	plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',s=100)

	# 隐藏坐标轴
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)


	# 将绘制图进行显示
	plt.show()

	keep_running = input("Make another walk?(y/n):")
	if keep_running == 'n':
		break
