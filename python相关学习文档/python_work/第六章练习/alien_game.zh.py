# coding:utf-8
# 创建一个空列表用来存储外星人
aliens=[]
# 用range()来创建多个外星人
for alien_number in range(30):
	new_alien={'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)
	
# 将前面三个外星人转变
for alien in aliens[0:3]:
	alien['color']='yellow'
	alien['points']=10
	alien['speed']='quick'

# 显示前五个外星人
for alien in aliens[0:5]:
	print(alien)
# 输出外星人的个数
print("The total numbers of aliens:"+str(len(aliens)))


