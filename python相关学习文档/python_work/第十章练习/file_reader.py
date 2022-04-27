# coding: utf_8
# 读取整个文件
# 函数open(需要寻找的文件名)是用来寻找和当前运行的python文件同目录的文件，注意是同目录 或者采用绝对路径也是可行的
# 用read()函数来读取需要寻找文件的全部内容，并将其作为一个长长的字符串存储在变量(此处为content)中
# 在使用read()函数读取过程中最后返回一个空字符串
with open('pi_digits.txt') as file_object:
	content = file_object.read()
	print(content)
# 采用绝对路径寻找文件
ab_rood='G:\python\python_work\第十章练习\pi_digits.txt'
with open(ab_rood) as file_object:
	#通过for循环对文件的每一行进行遍历，但每行会出现一行空白行
	for line in file_object:
		print(line)
# 可使用rstrip()函数消除多余的空白行
with open(ab_rood) as file_object:
	for line in file_object:
		print(line.rstrip())
# 使用了readline()函数和多个变量
with open(ab_rood) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line)
