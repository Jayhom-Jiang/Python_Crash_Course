# coding:utf-8
# �����б�Ԫ�ص��޸�
star=['mty','hj','xn','lyf','ym']
print(star)
star[2]='xr'
print(star)
# �����б�Ԫ�ص����
# �б���������Ԫ�ز��ã��б�.append('����ӵ�Ԫ��')����Ӱ���б�֮ǰ��Ԫ��
star.append('mla')
print(star)
# ���б��в���Ԫ�أ�����insert(��Ԫ�ص�������������ӵ�Ԫ�ء�)�������Ϳ������б��κδ������Ԫ��
star.insert(0,'mzd')
print(star)
# ���б���ɾ��Ԫ�أ�����del �б�[����]��ʹ�������������ɾ�������б���Ԫ�أ�ǰ����֪��������,����ʹ�����ַ�����û�з���ֵ
del star[0]
print(star)
# ���б���ɾ��Ԫ�أ����� �б�.pop()��ʹ������������ǰ��б�ĩβ��Ԫ�ص������൱�ڰ��б����ջ��Ȼ��pop�����ǳ�ջһ��
popped_star=star.pop()
print(star)
print(popped_star)
# ���б���ɾ��Ԫ�أ����� �б�.pop(����)��ʹ�������������ɾ���б����κ�λ�õ�Ԫ��
popped_star1=star.pop(1)
print(star)
print(popped_star1)
# ����ֵɾ��Ԫ�أ����õ�һ�ַ�ʽ �б�.remove('Ҫɾ����Ԫ��')������û�з���ֵ����һ�ַ�ʽ ����='Ҫɾ����Ԫ��' �б�.remove('����') �������ܹ��ñ�������ɾ����Ԫ�ص�ֵ ע�⣺remove����һ��ֻ��ɾ��һ����������ɾ������Ҫѭ��
favoriate_star='mty'
star.remove(favoriate_star)
print(favoriate_star)
print(star)

