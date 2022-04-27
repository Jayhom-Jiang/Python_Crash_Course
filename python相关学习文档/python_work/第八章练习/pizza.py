# coding: utf-8
# 当遇到不知道函数需要接受多少个实参时（任意数量实参），可采用：*变量 作为形参，其实就等同于一个元组
# 函数定义的形参变量就可以用处理元组的方法来处理
# 函数中若结合位置实参和任意数量实参时，在函数的形参表中先把位置实参放在前面，任意数量实参一般放到最后
def make_pizza(*toppings):
	"""打印顾客点的所有配料"""
	print(toppings)
	# 可以像处理元组一样处理形参变量
	for topping in toppings:
		print("pizza topping : "+topping)

make_pizza('beef')
make_pizza('beef','extra cheese','mushrooms')
