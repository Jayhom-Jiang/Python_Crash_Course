# coding:utf-8
# 用while循环同列表字典结合起来使用，可收集并存储大量输入
confirmed_user=['alice','bob','green']
unconfirmed_user=[]
while confirmed_user :
	# 用pop弹出元素，再用append加入元素
	current_user=confirmed_user.pop()
	print(current_user.title())
	unconfirmed_user.append(current_user)
print("The users have been unconfirmed :")
for users in unconfirmed_user:
	print(users.title())
