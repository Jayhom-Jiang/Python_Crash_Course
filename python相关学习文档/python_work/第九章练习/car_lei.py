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


my_car=Car('audi','a4','2018')
print(my_car.get_describe_name())
#通过方法来修改属性的值
my_car.update_odometer(18)
print("odometer_reading: "+str(my_car.get_odometer()))
#通过直接引用类对象的变量重新赋值来修改
my_car.odometer_reading=28
print("odometer_reading: "+str(my_car.get_odometer()))
# 路程回调的后果
my_car.update_odometer(18)
print("odometer_reading: "+str(my_car.get_odometer()))
