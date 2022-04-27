# coding:utf-8
# 排序列表中的元素：使用 列表.sort()方法，一旦使用就是永久性修改，下面是按照字母顺序重新排列
phone=['vivo','apple','mi','oppo']
phone.sort()
print(phone)
# 如果要用sort方法倒序排列则使用：列表.sort(reverse=True),然后就能够倒序排列,注意：必须是大写开头的True
phone.sort(reverse=True)
print(phone)
# 使用sorted()临时顺序排序：sorted(列表) 这样能够临时顺序排序但是不会对原来的列表顺序有任何的改变
print(sorted(phone))
print(phone)
# 使用sorted()临时倒序排序：sorted(列表,reverse=True) 这样能够临时倒序排序但是不会对原来的列表顺序有任何的改变
print(sorted(phone,reverse=True))
print(phone)
# 将原列表顺序倒序排列，也就是到这打印列表采用：列表.reverse() 也是属于永久性改变，但是恢复只需要再reverse翻转一次就行
phone.reverse()
print(phone)
# 计算列表的长度使用：len(列表) 因为python计数是从一开始所以结果不会相差1
print(len(phone))



