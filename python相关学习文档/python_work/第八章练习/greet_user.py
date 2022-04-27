# coding: utf-8
# 传递列表，像函数传递列表，列表通常包括名字、数字或更为复杂的对象字典
def great_users(names):
	"""向列表每位用户打招呼"""
	for name in names:
		sayhello="Hello, "+name.title()+" !"
		print(sayhello)
username=['xr','lmd','lz','hzz']
great_users(username)
