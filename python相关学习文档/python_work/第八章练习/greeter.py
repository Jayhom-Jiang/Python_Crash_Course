# coding: utf-8
# 向函数传递信息
# username是形参，'xr'是实参
def greet_users(username):
	print("Hello,"+username.title()+" !")
# 函数可以多次进行调用
greet_users('xr')
greet_users('lmd')
greet_users('lz')
greet_users('hzz')
#当需要传递多个实参时，要注意实参的顺序，一般是一一对应
def books(book_author_name,book_name):
	"""显示输出喜爱的书和作者"""
	print("Your favoriate book's author is :"+book_author_name)
	print("Your favoriate book's name is :"+book_name)
books('maboyong','The serects of three kingdoms')
print('\n')
books('The serects of three kingdoms','maboyong')

