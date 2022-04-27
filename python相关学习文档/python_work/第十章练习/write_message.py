# coding: utf-8
# 写入空文件
# 注意open(操作文件,模式) 'w' 写模式 'r'读模式(默认模式) 'a'附加模式(也就是在文件后面加上相应的内容) 'r+'读取写入都可模式 若操作文件在写模式下原文件存在那么后写入的内容会覆盖掉原文件的内容
# 若不存在那么会创建一个新文件用来进行操作
# 注意：python只能将字符串写入文本文件，若为数值数据类型采用str()函数转换
with open('programming.txt','w') as file_object:
	#用write()函数进行文件写操作,需要自己添加换行符进行换行
	file_object.write("I LOVE PROGRAMMING!\n")
	file_object.write("I LOVE PROGRAMMING，too!\n")
	# 友好提示
	print("写入文件成功")

with open('programming.txt','a') as file_object:
	#用write()函数进行文件写操作,需要自己添加换行符进行换行
	file_object.write("I LOVE PROGRAMMING,too too!\n")
	file_object.write("I LOVE PROGRAMMING，too too too!\n")
	# 友好提示
	print("写入文件成功")

