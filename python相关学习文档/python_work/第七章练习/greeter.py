# coding:utf-8
prompt = "If you tell us who you are,we can personalize the messages you see."
prompt+="\nWhat is your fist name? :"
name = input(prompt)
print("\nYour first name is : "+name.title())
# 若需要用户输入的整型之类的数据类型，采用int()函数将python将输入视为数值
age = input("Please input your age:")
age=int(age)
print(age)
if(age >= 18):
	print("You are a adult!")
else:
	print("You are not a adult!")

