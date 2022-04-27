# coding: utf-8
# while循环的条件语句不局限于运算比较符
pets=['cat','dog','monkey','cat','fish','pig','tiger','dog','cat']
print(pets)
while 'cat' in pets :
	pets.remove('cat')
print(pets)
