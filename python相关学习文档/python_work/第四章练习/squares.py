# coding:utf-8
# ����ı�ʾ���б�
squares=[]
for value in range(1,11):
# ������ʹ�ñ�����������˵Ĵ���Ƚ�����ѡ��
	squares.append(value**2)
print(squares)
# �б������ʽ�������б��뷽ʽ��ע���ʽ: �б�[���ʽ forѭ��] ע��forѭ������û��ð�ţ�
squares=[value**2 for value in range(1,11)]
print(squares)
