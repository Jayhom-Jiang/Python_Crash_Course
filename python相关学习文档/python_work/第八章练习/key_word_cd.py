# coding: utf-8
# 关键字实参让我们无需考虑函数调用中的实参顺序
def describe_pets(animal_type,animal_name):
	"""显示宠物的信息"""
	print("animal_type: "+animal_type)
	print("animal_name: "+animal_name)
# 关键字实参就是在函数参数传递过程中，在调用函数时将 形参名=‘实参传递的值’ 这种形式
# 下面两个调用函数输出结果是一样的
describe_pets(animal_type='dog',animal_name='泰迪')
print('\n')
describe_pets(animal_name='泰迪',animal_type='dog')

# 默认值的使用：在编写函数时，可给形参指定默认参数
def describe_pets(animal_type,animal_name='二哈'):
	"""显示宠物的信息"""
	print("animal_type: "+animal_type)
	print("animal_name: "+animal_name)
# 若调用函数提供了实参就覆盖原函数定义的默认参数，若没有则使用形参指定的默认参数
describe_pets(animal_type='dog',animal_name='泰迪')
print('\n')
# 下面的函数调用没有指定默认参数
describe_pets(animal_type='dog')
print('\n')
# 在使用默认值时，在形参列表中必须先列出没有默认值的形参，在列出有默认值的形参，这样便于python能够正确解读位置实参
# 个人总结：就是把没有默认值的放定义函数前面排，有默认值的放后面排
describe_pets('cat')

