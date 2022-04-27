# coding:utf-8
# 在字典中存储的列表
pizza={
	'crust':'thick',
	'toppings':['egg','cheese'],
	}
print("crust:"+pizza['crust'])
# 因为字典中存储的第二个键-值对是列表所以如果要输出列表元素还是得用for循环输出
# 每当需要在字典中将一个键关联到多个值时，都可以在字典中的键嵌套一个列表
# 字典嵌套列表或者列表嵌套字典，不宜嵌套太多
for topping in pizza['toppings']:
	print(topping)
# 字典中嵌套字典，尽量不要嵌套太多处理比较麻烦,也就是键-字典(值)
user={
	'aeinsterin':{
		'first':'ru',
		'last':'xie',
		'location':'shaoyang',
		},
	'mcurie':{
		'first':'yong',
		'last':'xie',
		'location':'beijing',
		},
	}
# user_info 因为通过大字典的items()方法获得了大字典的值，而大字典的值也是字典，所以user_info的数据类型也是字典
for name,user_info in user.items():
	print(name)
	print(user_info['location'])

