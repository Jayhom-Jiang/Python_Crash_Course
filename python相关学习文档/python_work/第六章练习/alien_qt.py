# coding:utf-8
# 嵌套，可以将一系列字典存储在列表中，以字典作为列表元素存储，此列表叫做字典列表
alien_0={'color':'green','points':5}
alien_1={'color':'blue','points':4}
alien_2={'color':'red','points':6}

aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
	print(alien)
