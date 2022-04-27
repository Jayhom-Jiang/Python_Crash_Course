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

# 继承
class Electric_car(Car):
	"""电动汽车的独特之处"""

	def __init__(self,make,model,year):
		"""初始化父类的属性,同时电动车也可以有自己的特有的属性和方法"""
		# super()是一个特殊得函数，将父类和子类联系起来，用__init__()这个方法使子类包含父类的所有属性
		super().__init__(make,model,year)
		self.battery=Battery()


#将实例用作属性
class Battery():
	"""一次模拟电动车电瓶的简单尝试"""
	def __init__(self,battery_size=70):
		self.battery_size=battery_size

	def describe_battery(self):
		"""打印一条描述电瓶容量的消息"""
		print("battery_size: "+str(self.battery_size))

# 首先是子类创建对象，然后子类对象引用子类的变量a，但注意变量a是另一个类的对象b，然后再通过 变量a（对象b）引用 类（对象b的类）的方法
my_tesal=Electric_car('tesal','a4','2018')
my_tesal.battery.describe_battery()
