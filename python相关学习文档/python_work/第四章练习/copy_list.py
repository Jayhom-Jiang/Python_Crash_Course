# coding:utf-8
# 复制列表的副本到另一个列表，复制之后两者之间并不影响
my_food=['beef','chicken','duck']
# 注意复制副本方式为：列表=副本列表[:]
friend_food=my_food[:]
print(my_food)
print(friend_food)
my_food.append('ice')
friend_food.append('eggs')
print(my_food)
print(friend_food)

# 当用这种方式去复制时：列表=列表 这两个列表是指向同一个列表，所以一个变都会变
games=['wz','cy','dgsd','seh']
games1=[]
games1=games
print(games)
print(games1)
games.append('mezy')
games1.append('tcs')
print(games)
print(games1)






