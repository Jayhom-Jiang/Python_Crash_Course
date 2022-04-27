# coding:utf-8
# 第一种方式功能不易扩展
#import json
# 如果以前存储了用户名，就加载它
#filename="username.json"
#try:
	#with open(filename) as file_object:
		#username=json.load(file_object)
		# 若没有存储就提示用户输入然后之后第二次运行再加载用户名
#except FileNotFoundError:
	#username=input("Please input your name : ")
	#with open(filename,'w') as file_object:
		#json.dump(username,file_object)
		#print("I remember your name :"+username)
#else:
	#print("Welcome back , "+username+" !")

# 第二种方式易于扩展
import json
# 用来调用已存储用户
def get_stored_username():
	"""如果用户存储了用户名就获取它"""
	filename="username.json"
	try:
		with open(filename) as file_object:
			username=json.load(file_object)

	except FileNotFoundError:
		return None
	else:
		return username

def get_newusername():
	"""原来没有存储用户，所以提示存储新用户"""
	filename="username.json"
	username=input("Please input your name : ")
	with open(filename,'w') as file_object:
		json.dump(username,file_object)
	return username

def greet_username():
	"""问候新用户并输出新用户的名字"""
	username=get_stored_username()
	if username:
		print("Welcome back , "+username+" !")
	else:
		username=get_newusername()
		print("I remember your name :"+username)

greet_username()
