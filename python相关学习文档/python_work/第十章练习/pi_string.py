# coding: utf-8
# 使用文件的内容，读取文本文件的内容之后可以对内容进行重新编辑
# 对于可处理的数据python本身没有任何限制，只要系统内存够多
ab_rood='G:\python\python_work\第十章练习\pi_million_digits.txt'
with open(ab_rood) as file_object:
	lines = file_object.readlines()

pi_string=''
for line in lines:
	pi_string+=line.strip()

print(pi_string)
print(len(pi_string))

birthday = input("Please input your birthday :")
# 用if语句和in来判断存在与否
if birthday in pi_string:
	print("你的生日在圆周率里")
else:
	print("你的生日不在圆周率里")
