# coding:utf-8
# 这是列表元素的修改
star=['mty','hj','xn','lyf','ym']
print(star)
star[2]='xr'
print(star)
# 这是列表元素的添加
# 列表在最后添加元素采用：列表.append('新添加的元素')不会影响列表之前的元素
star.append('mla')
print(star)
# 在列表中插入元素：采用insert(新元素的索引，‘新添加的元素’)，这样就可以在列表任何处添加新元素
star.insert(0,'mzd')
print(star)
# 在列表中删除元素：采用del 列表[索引]，使用这个方法可以删除所有列表中元素，前提是知道其索引,并且使用这种方法是没有返回值
del star[0]
print(star)
# 在列表中删除元素：采用 列表.pop()，使用这个方法就是把列表末尾的元素弹出就相当于把列表比作栈，然后pop方法是出栈一样
popped_star=star.pop()
print(star)
print(popped_star)
# 在列表中删除元素：采用 列表.pop(索引)，使用这个方法可以删除列表中任何位置的元素
popped_star1=star.pop(1)
print(star)
print(popped_star1)
# 根据值删除元素，采用第一种方式 列表.remove('要删除的元素')，这样没有返回值；第一种方式 变量='要删除的元素' 列表.remove('变量') 这样就能够用变量保存删掉的元素的值 注意：remove方法一次只能删除一个，若想多个删除则需要循环
favoriate_star='mty'
star.remove(favoriate_star)
print(favoriate_star)
print(star)

