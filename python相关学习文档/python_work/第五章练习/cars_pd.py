# coding:utf-8
# �������������ж���if-else����ʽ�������5-9�д��룬ע�������ð��(��)
cars=['bm','Bc','lsls','fll']
for car in cars:
	if car == 'fll':
		print("This is a nb car!")
	else:
		print("just so so!")
# �������ԣ��ж����Ϊtrue����false�������,�����У�����(==)��������(!=)��С��(<)[�жϴ�Сֻ���������ֱȽ�]���������������������ƣ���Ҫע����ǣ������жϴ�Сд����
# �ڱȽ���������߸����һ���ո������������Ķ����
for car1 in cars:
	#print(car1 == 'fll')
	#print(car1 != 'bm')
	print(car1=='Fll')
# ��Щ��վΪ�˱�֤�û����Ķ�һ�޶����Ὣ�û�����Сд��ĸ�洢(�ú���lower())��Ȼ���ٽ���ƥ��
for car2 in cars:
	if(car2.lower() == 'bc'):
		print("There is a bc car!")
	else:
		print("No bc car!")
# ���ж��������Ҫ��飬������and ���� or
numbers=list(range(1,11))
for number in numbers:
	#if number>1 and number<=5:
		#print(number)
	if number<=9 or number<10:
		print(number)
# ����ض�ֵ�Ƿ�������߲��������б����ùؼ��� in ���� not in
min_number=1
max_number=11
if min_number in numbers:
	print("The min number is 1 ")
if max_number not in numbers:
	print("The max number do not exist")

# ���ж��������Ҫ�ж�ʱ������if-elif-else������� ���߲��Զ������if-if-if
for car3 in cars:
	if car3 == 'bm':
		print("bm car")
	elif car3 == 'fll':
		print("fll car")
	elif car3.lower() == 'bc':
		print("bc car")
	else:
		print("others car")
# ȷ���б��ǿյ�,�����ã�if �б�
accounts=[]
if accounts:
	for account in accounts:
		print(account)
else:
	print("The account is empty!")	
	
	
	
