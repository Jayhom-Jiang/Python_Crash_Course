# coding:utf-8
# ��Ȼpython���ں���-ֵ�Ե�����˳�򣬵��������Ҫ����˳������������ɲ���sorted()����
favoriate_friut={
	'xr':'banana',
	'lmd':'apple',
	'lz':'orange',
	'hzz':'flower',
	'lhm':'banana'
	}
print(favoriate_friut)
# ��˳�����������ȡ�ĸ�ʽ�� sorted(�ֵ�.keys())
for people in sorted(favoriate_friut.keys()):
	print(people.title())
# keys()�����������������values()�������������ֵ
for friut in sorted(favoriate_friut.values()):
	print(friut.title())
# ����Ҫ�޳��ֵ�����ظ�����ã�set()����
for friut in set(favoriate_friut.values()):
	print(friut.title())

