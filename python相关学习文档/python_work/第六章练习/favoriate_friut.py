# coding:utf-8
# 虽然python不在乎键-值对的排列顺序，但是如果需要按照顺序排列输出，可采用sorted()方法
favoriate_friut={
	'xr':'banana',
	'lmd':'apple',
	'lz':'orange',
	'hzz':'flower',
	'lhm':'banana'
	}
print(favoriate_friut)
# 按顺序排列输出采取的格式： sorted(字典.keys())
for people in sorted(favoriate_friut.keys()):
	print(people.title())
# keys()方法是用来输出键，values()方法是用来输出值
for friut in sorted(favoriate_friut.values()):
	print(friut.title())
# 若想要剔除字典输出重复项，采用：set()方法
for friut in set(favoriate_friut.values()):
	print(friut.title())

