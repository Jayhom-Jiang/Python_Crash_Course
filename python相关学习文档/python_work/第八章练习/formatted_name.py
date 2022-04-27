# coding: utf-8
# 定义函数用return返回值 用法：return 返回的内容
def get_formatted_name(first_name,last_name):
	"""返回整个姓名"""
	full_name=first_name+" "+last_name
	return full_name.title()
# 调用函数有返回值时需要定义另一个变量去接受这个返回值 比如：变量=函数(有实参或者没有实参)
full_name1=get_formatted_name('xie','ru')
print(full_name1)
