# coding: utf-8
# 处理ZeroDivisionError异常
print("异常发生前")
try:
	# 发生异常后直接跳转到except执行，然后就再直接从except后面执行了
	print(5/0)
	print(异常发生中)
	# 告诉python系统如何去解决ZeroDivisionError这种异常
except ZeroDivisionError:
	print("You can not divide the zero")
print("异常发生后")
