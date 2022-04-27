# coding: utf-8
# 让实参变成可选
# 因为中间名有默认参数所以应该放到最后，同时以中间名来作为可选项
def get_formatted_name(first_name,last_name,middle_name=''):
	"""返回完整的姓名"""
# 若调用函数没有传来实参，那么默认参数是空就会执行else语句
	if middle_name:
		full_name=first_name+" "+middle_name+" "+last_name
	else:
		full_name=first_name+" "+last_name
# title()函数只会将整个字符串的首字母变成大写，若有空格则分割
	return full_name.title()
name=get_formatted_name("xie","ru")
print(name)
print("\n")
name=get_formatted_name(first_name="l",middle_name="h",last_name="l")
print(name)
