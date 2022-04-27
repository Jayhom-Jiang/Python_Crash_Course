# coding: utf-8
# 绘制散点图并设置其样式
import matplotlib.pyplot as plt
# 使用scatter()描绘散点,并且使用实参s设置了绘制图形的点的尺寸
#x_values = [1,2,3,4,5]
#y_values = [1,4,9,16,25]

# 自己设置比较麻烦，可以让python来为我们进行计算
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
# 由于点数太多所以设置的点的大小不要设置太大,修改颜色
#plt.scatter(x_values,y_values,c='red',edgecolor='none',s=40)
# 是用颜色映射
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=40)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Number",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of value",fontsize=14)

# 设置刻度标记大小,axis默认情况下是对xy轴同时起作用进行同样的设置(也就是后面的参数比如字体大小颜色等)，当是你也可以分开设置
plt.tick_params(axis='both',which='major',labelsize=14)

# 设置每个坐标轴的范围,x的范围是0到1100，y的范围是0到11000000
plt.axis([0,1100,0,1100000])

# 自动保存图表,第一个参数是指以什么形式和文件名保存图表到此文件目录中，后面的参数是裁剪图表多余的空白区域，且代码需要放在显示前面
plt.savefig('squares_plot.png',bbox_inches='tight')

# 显示散点图
plt.show()


