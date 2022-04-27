# coding: utf-8
print("Please input two numbers , I will divide two numbers!")
print("Enter 'q' to quit the exe!")

while True:
	first_number=input("\n First_number:")
	if(first_number=='q'):
		break;
	Second_number=input("\n Second_number:")
	if(Second_number=='q'):
		break;
	try:
		answer=int(first_number)/int(Second_number)
	except ZeroDivisionError:
		print("You can not divide the zero")
	# else代码块是依赖于try代码块成功执行的代码放到else代码块，也就是try没有发生异常就执行else代码块的内容
	else:
		print(answer)

