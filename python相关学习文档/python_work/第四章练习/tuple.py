# coding:utf-8
# 元组的定义是：元组=(元组元素，元组元素) 元组的修改必须是重新将元组全部重新赋值，不能只修改一个,除此以外和列表的用法差不多
# tuple(列表)：将暂时将列表转换为元组,但是如果单独输出列表还是不会改变   个人理解：披着元组外皮的列表本质还是列表，脱下皮就显出原形了
# 元组中只包含单个元素时，需要在该元素后面添加逗号
singers=('mty','ldh','zxy','zjl','wf')
for singer in singers:
    print(singers[0])
    print(singer)
# singers[0]='fqf',对元组这么赋值是有问题的，程序会报错，但是下面如果对元组重新赋值就不会错
singers=['mty']
print(singers)
