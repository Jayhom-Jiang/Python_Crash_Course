# coding:utf-8
# �����б��е�Ԫ�أ�ʹ�� �б�.sort()������һ��ʹ�þ����������޸ģ������ǰ�����ĸ˳����������
phone=['vivo','apple','mi','oppo']
phone.sort()
print(phone)
# ���Ҫ��sort��������������ʹ�ã��б�.sort(reverse=True),Ȼ����ܹ���������,ע�⣺�����Ǵ�д��ͷ��True
phone.sort(reverse=True)
print(phone)
# ʹ��sorted()��ʱ˳������sorted(�б�) �����ܹ���ʱ˳�������ǲ����ԭ�����б�˳�����κεĸı�
print(sorted(phone))
print(phone)
# ʹ��sorted()��ʱ��������sorted(�б�,reverse=True) �����ܹ���ʱ���������ǲ����ԭ�����б�˳�����κεĸı�
print(sorted(phone,reverse=True))
print(phone)
# ��ԭ�б�˳�������У�Ҳ���ǵ����ӡ�б���ã��б�.reverse() Ҳ�����������Ըı䣬���ǻָ�ֻ��Ҫ��reverse��תһ�ξ���
phone.reverse()
print(phone)
# �����б�ĳ���ʹ�ã�len(�б�) ��Ϊpython�����Ǵ�һ��ʼ���Խ���������1
print(len(phone))



