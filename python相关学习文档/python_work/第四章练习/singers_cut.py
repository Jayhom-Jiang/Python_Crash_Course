# coding:utf-8
# 列表的部分元素的输出叫做切片，方法是：列表[列表起始元素索引，终止元素的索引加1]
singers=['mty','ny','wf','zjl']
print(singers[0:3])
# 若切片没有指定结束元素那么将会一直到列表的最后一个元素
print(singers[1:])
# 若切片没有指定起始元素，那么就从列表中第一个元素开始
print(singers[:3])
# 若切片都没有指定那么就把列表所有元素全部输出
print(singers[:])
# 若切片起始位置是负数(-a)，那么就从倒数的a开始到列表元素最后
print(singers[-2:])
print(singers)
