# coding: utf-8
# return可以返回任何类型值，包括列表和字典等比较复杂的数据类型
# 给函数增加了一个可选参数age
def person_dic(first_name,last_name,age=''):
	"""返回一个字典，其中包含一个人的姓名"""
	person={'first':first_name,'last':last_name}
	if age:
		person['age']=age
	#返回了字典
	return person
person1=person_dic("xie","ru")
print(person1)
person2=person_dic("xie","ru",18)
print(person2)
