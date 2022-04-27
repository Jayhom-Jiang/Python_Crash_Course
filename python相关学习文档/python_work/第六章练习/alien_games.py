# coding:utf-8
# 修改字典中键-值对的值
alien_0={'x_position':0,'y_position':25,'speed':'medium'}
print("Original x_position:\n"+str(alien_0['x_position']))
# 根据字典中外星人的速度值进行匹配然后相应的移动
# 可以通过修改键值来改变外星人的行为
alien_0['speed']='fast'
if alien_0['speed']=='slow':
	x_increment=1
elif alien_0['speed']=='medium':
	x_increment=2
else:
	x_increment=3
alien_0['x_position']=alien_0['x_position']+x_increment
print("New x_position:\n"+str(alien_0['x_position']))
