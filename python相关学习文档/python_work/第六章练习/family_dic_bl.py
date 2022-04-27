# coding:utf-8
# 遍历字典的键-值对
family={
	'grandfather':'xlh',
	'grandmother':'mgy',
	'father':'xyj',
	'mother':'hqf',
	'son':'xr',
	}
# 前面访问键-值对都是通过键来访问值，如果键值都要访问就可以采用：for循环，然后加上item方法
# 具体格式: for k,y in 字典.items(): 每次遍历的结果都和键-值对的输入顺序不一样，所以每次运行的输出结果也不一样
for key,value in family.items():
	print("\nkey:"+key)
	print("value:"+value)
# 假如是只遍历键，那么可以直接用keys()方法或者不用但建议使用便于程序易读：for k in 字典.keys():
for key in family.keys():
	print("\nkey:"+key)
# 方法keys()并非只能用来遍历，实际上它返回一个列表包含了相应字典的所有键
if 'son' in family.keys():
	print("key son in family")
