# coding:utf-8
# ����һ�����б������洢������
aliens=[]
# ��range()���������������
for alien_number in range(30):
	new_alien={'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)
	
# ��ǰ������������ת��
for alien in aliens[0:3]:
	alien['color']='yellow'
	alien['points']=10
	alien['speed']='quick'

# ��ʾǰ���������
for alien in aliens[0:5]:
	print(alien)
# ��������˵ĸ���
print("The total numbers of aliens:"+str(len(aliens)))


