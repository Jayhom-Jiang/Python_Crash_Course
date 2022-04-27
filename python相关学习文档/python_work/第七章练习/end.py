# coding: utf-8
#第一种方法
# 给pd赋初值主要是为了让while循环有判断的依据，所以必须提前定义并且赋初值，否则python没法继续执行
#pd=""
#while pd != 'quit' :
	#pd=input("Please input 'quit' to end the program :")
#print("The game over")

# 第二种采用标志位用“True”或者“false”来控制程序的执行和结束
#flag = True
#while flag :
	#pd=input("Please input 'quit' to end the program :")
	#if pd == 'quit':
		#flag = False
#print("The game over")

# 第三种方法使用break跳出循环
while True :
	pd=input("Please input 'quit' to end the program :")
	if pd == 'quit':
		break;
print("The game over")

# 第三种方法使用continue跳出当前一次循环，但并没有退出循环
while True :
	pd=input("Please input 'quit' to end the program :")
	if pd == 'quit':
		continue;
	print('Not quit')
print("The game over")
