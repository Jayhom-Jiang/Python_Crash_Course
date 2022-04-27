# coding:utf-8
# 函数range(a,b)只能从(a)一直到(b-1)而不是到(b)
for value in range(1,5):
	print(value)
# 我们可以用list函数将range函数生成的数字变成一个个列表元素，存放在列表中
numbers=list(range(1,6))
print(numbers)
# 函数range(a,b,c)表示的是从(a)开始一直到大于等于(b)，但是每一次都是加上(c)
two_numbers=list(range(2,10,2))
print(two_numbers)

