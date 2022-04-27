# coding: utf-8
# 在python中大写字母开头的一般是类 如：Dog()
class Dog():
	"""一次模拟小狗的尝试"""
	# __init__(前后两个下划线否则会报错)是一个特殊的方法类似于其他类语言中的构造函数
	# self是一个指向实例本身的应用（自动的）必须要存在每一个方法，所以用类只需要传递其它的形参
	def __init__(self,name,age):
		"""初始化小狗的姓名和年龄"""
		self.name=name
		self.age=age
	def sit(self):
		"""模拟小狗的动作蹲下"""
		print(self.name+" sitting down!")
	def roll_over(self):
		"""模拟小狗打滚"""
		print(self.name+" is rolled over!")
# 根据类创建实例，要注意__init__(self,参数，参数，....)参数的个数，根据这个个数来创建实例
my_dog=Dog('小强','12')
# 要访问实例的属性，可以使用句点表示法 ： 类实例.属性
print(my_dog.name)
# 调用类的方法就采用：类实例.方法名()
my_dog.sit()
my_dog.roll_over()
# 创建多个实例也是可以的也就是同一个类可以创建多个对象
your_dog=Dog('小白',13)
print(your_dog.name)
