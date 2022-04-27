# coding:utf-8
# 一个简单的字典，注意字典的格式键-值对：字典={字典键：字典值，字典键：字典值}
# 若要访问字典中的值就必须先获取键，采用：字典[想要访问的值所对应的键]
alien_0={'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
# python学习有感：虽然在python中创建变量不用指明变量数据类型，但同时也默认了变量数据类型与它被赋初值的数据类型一致，比如变量a=5，那么变量a就是整型
new_points=alien_0['points']
print("points:"+str(new_points))
# 添加键-值对的方法：字典['键名']=键名的值
# 注意：键-值对的排列顺序与添加顺序不同，python不关心键-值对的添加顺序
alien_0['x_position']=0
alien_0['y_position']=25
# 修改字典中的值：字典['原键']=‘键名的值’
alien_0['color']='blue'
print(alien_0)
# 可以先创建一个空字典:字典={}，再往里面添加键-值对：字典['键名']=键名的值
singer={}
singer['name']='xr'
singer['sex']='man'
print(singer)


