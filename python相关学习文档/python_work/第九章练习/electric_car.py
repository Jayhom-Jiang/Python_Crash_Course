# coding: utf-8
class Car():
	"""一次模拟汽车的简单尝试"""
	def __init__(self,make,model,year):
		"""初始化描述汽车的属性"""
		self.make=make
		self.model=model
		self.year=year
		# 给属性指定默认值，在__init__()方法是可行的，若对某属性做了，这样之后就就无需包含为它提供初始值的形参
		self.odometer_reading=0
	def get_describe_name(self):
		"""返回整洁的描述信息"""
		name=str(self.year)+" "+self.model+" "+self.make
		return name
	def get_odometer(self):
		"""返回车子的行驶路程"""
		return self.odometer_reading
	#修改属性的值 1、通过直接引用类对象的变量重新赋值来修改 2、通过方法来修改属性的值
	def update_odometer(self,odometer):
		"""通过方法来修改属性的值"""
		"""禁止路程回调"""
		if(odometer > self.odometer_reading):
			self.odometer_reading=odometer
		else:
			print("NO roll back!")


# 继承
class Electric_car(Car):
	"""电动汽车的独特之处"""

	def __init__(self,make,model,year):
		"""初始化父类的属性,同时电动车也可以有自己的特有的属性和方法"""
		# super()是一个特殊得函数，将父类和子类联系起来，用__init__()这个方法使子类包含父类的所有属性
		super().__init__(make,model,year)
		self.battery_size=70

	# 定义电动车自己独特的方法
	def describe_battery(self):
		"""打印一条描述电瓶容量的消息"""
		print("battery_size: "+str(self.battery_size))

	def get_describe_name(self):
		"""返回整洁的描述信息"""
		name="New ways :"+str(self.battery_size) 和
		return name

# 子类对象的创造和定义子类的方法要参数对应
my_electric_car=Electric_car('audi','b3',10)
# 子类对象可以通过调用父类的方法来获得一些结果
print(my_electric_car.get_describe_name())
# 子对象引用自己类独特的方法
my_electric_car.describe_battery()
# 子类还可以重写父类方法，前提是保证函数名和参数一致
print(my_electric_car.get_describe_name())
