# coding:utf-8
# ���ֵ��д洢���б�
pizza={
	'crust':'thick',
	'toppings':['egg','cheese'],
	}
print("crust:"+pizza['crust'])
# ��Ϊ�ֵ��д洢�ĵڶ�����-ֵ�����б��������Ҫ����б�Ԫ�ػ��ǵ���forѭ�����
# ÿ����Ҫ���ֵ��н�һ�������������ֵʱ�����������ֵ��еļ�Ƕ��һ���б�
# �ֵ�Ƕ���б�����б�Ƕ���ֵ䣬����Ƕ��̫��
for topping in pizza['toppings']:
	print(topping)
# �ֵ���Ƕ���ֵ䣬������ҪǶ��̫�ദ��Ƚ��鷳,Ҳ���Ǽ�-�ֵ�(ֵ)
user={
	'aeinsterin':{
		'first':'ru',
		'last':'xie',
		'location':'shaoyang',
		},
	'mcurie':{
		'first':'yong',
		'last':'xie',
		'location':'beijing',
		},
	}
# user_info ��Ϊͨ�����ֵ��items()��������˴��ֵ��ֵ�������ֵ��ֵҲ���ֵ䣬����user_info����������Ҳ���ֵ�
for name,user_info in user.items():
	print(name)
	print(user_info['location'])

