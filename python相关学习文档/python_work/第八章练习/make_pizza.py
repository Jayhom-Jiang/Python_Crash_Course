# coding: utf-8
# 将函数存储在模块中
# 使用任意数量的关键字实参
# 传递无数关键字实参采用： **变量 然后这个变量就等同于字典
# 然后我们可以用操作字典的方法来进行处理键-值对
def maked_pizza(*toppings):
	"""打印顾客点的所有配料"""
	print(toppings)
	# 可以像处理元组一样处理形参变量
	for topping in toppings:
		print("pizza topping : "+topping)
