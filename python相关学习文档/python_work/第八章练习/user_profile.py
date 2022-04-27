# coding: utf-8
# 使用任意数量的关键字实参
# 传递无数关键字实参采用： **变量 然后这个变量就等同于字典
# 然后我们可以用操作字典的方法来进行处理键-值对
def build_profile(first,last,**user_info):
	"""创建一个字典，其中包含我们知道的有关用户的一切"""
	profile={}
	profile['firet_name']=first.title()
	profile['last_name']=last.title()
	for k,v in user_info.items():
		profile[k]=v
	# 我们可以返回这个字典
	return profile

user_profile=build_profile('xie','ru',location='shaoyang',field='IT')
print(user_profile)
