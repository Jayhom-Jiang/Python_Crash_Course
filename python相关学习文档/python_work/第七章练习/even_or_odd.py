# coding:utf-8
# 整个流程描述一下：首先输入一个数，然后input()函数默认为是字符串，然后用int()函数把字符串转换为int型，然后输出中用str()函数转换为字符串
number=input("Enter a number, and I'll tell you if it's even or odd:")
number=int(number)

if number%2==0:
	print("\nThe number "+str(number)+" is even")
else:
	print("\nThe number "+str(number)+" is odd")
