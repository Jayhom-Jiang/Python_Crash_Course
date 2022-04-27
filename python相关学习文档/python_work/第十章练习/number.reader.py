# coding: utf-8
# 存储数据
import json
filename="number.json"
with open(filename) as file_object:
	#json.load()函数接受一个实参，就是用来加载需要加载数据的文件对象
	number=json.load(file_object)
print(number)
