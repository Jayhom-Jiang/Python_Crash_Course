# coding: utf-8
# 存储数据使用json模块
import json

number=[1,2,3,4,5,6,7,8,9]
filename="number.json"
with open(filename,'w') as file_object:
	# json.dump()函数接受两个实参，一个是要存储的数据一个是用于存储数据的文件对象
	json.dump(number,file_object)
	print("成功写入")
