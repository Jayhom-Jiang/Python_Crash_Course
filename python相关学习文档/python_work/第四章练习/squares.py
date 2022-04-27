# coding:utf-8
# 下面的表示空列表
squares=[]
for value in range(1,11):
# 尽量少使用变量，简洁明了的代码比较优先选择
	squares.append(value**2)
print(squares)
# 列表解析方式采用两行编码方式，注意格式: 列表[表达式 for循环] 注意for循环后面没有冒号：
squares=[value**2 for value in range(1,11)]
print(squares)
