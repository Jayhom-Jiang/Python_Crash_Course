# coding: utf-8
# 绘制简单折线图
# 导入模块pyplot
import matplotlib.pyplot as plt
# 提供输入数值，以保证结果一一对应正确输出
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
# 将输入输出列表中的传递给函数plot,linewidth参数决定了线条的粗细
plt.plot(input_values,squares,linewidth=5)

# 设置图表标题，并给坐标轴上贴上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of value",fontsize=14)

# 设置刻度标记大小
plt.tick_params(axis='both',labelsize=14)

# plt.show()函数可以打开matplotlib查看器
plt.show()
