# coding:utf-8
# �����ֵ�ļ�-ֵ��
family={
	'grandfather':'xlh',
	'grandmother':'mgy',
	'father':'xyj',
	'mother':'hqf',
	'son':'xr',
	}
# ǰ����ʼ�-ֵ�Զ���ͨ����������ֵ�������ֵ��Ҫ���ʾͿ��Բ��ã�forѭ����Ȼ�����item����
# �����ʽ: for k,y in �ֵ�.items(): ÿ�α����Ľ�����ͼ�-ֵ�Ե�����˳��һ��������ÿ�����е�������Ҳ��һ��
for key,value in family.items():
	print("\nkey:"+key)
	print("value:"+value)
# ������ֻ����������ô����ֱ����keys()�������߲��õ�����ʹ�ñ��ڳ����׶���for k in �ֵ�.keys():
for key in family.keys():
	print("\nkey:"+key)
# ����keys()����ֻ������������ʵ����������һ���б��������Ӧ�ֵ�����м�
if 'son' in family.keys():
	print("key son in family")
