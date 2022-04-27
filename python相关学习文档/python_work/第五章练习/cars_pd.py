# coding:utf-8
# 对于两种条件判断用if-else，格式见下面的5-9行代码，注意别忘记冒号(：)
cars=['bm','Bc','lsls','fll']
for car in cars:
	if car == 'fll':
		print("This is a nb car!")
	else:
		print("just so so!")
# 条件测试，判断语句为true或者false两种情况,条件有：等于(==)，不等于(!=)，小于(<)[判断大小只适用于数字比较]等这个和其它编程语言类似，需要注意的是：条件判断大小写敏感
# 在比较运算符两边各添加一个空格，这样更容易阅读理解
for car1 in cars:
	#print(car1 == 'fll')
	#print(car1 != 'bm')
	print(car1=='Fll')
# 有些网站为了保证用户名的独一无二，会将用户名以小写字母存储(用函数lower())，然后再进行匹配
for car2 in cars:
	if(car2.lower() == 'bc'):
		print("There is a bc car!")
	else:
		print("No bc car!")
# 当有多个条件需要检查，可以用and 或者 or
numbers=list(range(1,11))
for number in numbers:
	#if number>1 and number<=5:
		#print(number)
	if number<=9 or number<10:
		print(number)
# 检查特定值是否包含或者不包含在列表中用关键字 in 或者 not in
min_number=1
max_number=11
if min_number in numbers:
	print("The min number is 1 ")
if max_number not in numbers:
	print("The max number do not exist")

# 当有多个条件需要判断时，采用if-elif-else这种情况 或者测试多个条件if-if-if
for car3 in cars:
	if car3 == 'bm':
		print("bm car")
	elif car3 == 'fll':
		print("fll car")
	elif car3.lower() == 'bc':
		print("bc car")
	else:
		print("others car")
# 确定列表不是空的,就是用：if 列表：
accounts=[]
if accounts:
	for account in accounts:
		print(account)
else:
	print("The account is empty!")	
	
	
	
