# coding:utf-8
# ��whileѭ��ͬ�б��ֵ�������ʹ�ã����ռ����洢��������
confirmed_user=['alice','bob','green']
unconfirmed_user=[]
while confirmed_user :
	# ��pop����Ԫ�أ�����append����Ԫ��
	current_user=confirmed_user.pop()
	print(current_user.title())
	unconfirmed_user.append(current_user)
print("The users have been unconfirmed :")
for users in unconfirmed_user:
	print(users.title())
