# coding: utf-8
#��һ�ַ���
# ��pd����ֵ��Ҫ��Ϊ����whileѭ�����жϵ����ݣ����Ա�����ǰ���岢�Ҹ���ֵ������pythonû������ִ��
#pd=""
#while pd != 'quit' :
	#pd=input("Please input 'quit' to end the program :")
#print("The game over")

# �ڶ��ֲ��ñ�־λ�á�True�����ߡ�false�������Ƴ����ִ�кͽ���
#flag = True
#while flag :
	#pd=input("Please input 'quit' to end the program :")
	#if pd == 'quit':
		#flag = False
#print("The game over")

# �����ַ���ʹ��break����ѭ��
while True :
	pd=input("Please input 'quit' to end the program :")
	if pd == 'quit':
		break;
print("The game over")

# �����ַ���ʹ��continue������ǰһ��ѭ��������û���˳�ѭ��
while True :
	pd=input("Please input 'quit' to end the program :")
	if pd == 'quit':
		continue;
	print('Not quit')
print("The game over")
