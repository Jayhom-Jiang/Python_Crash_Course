# coding: utf-8
# return可以返回任何类型值，包括列表和字典等比较复杂的数据类型
def person_dic(first_name,last_name):
	"""返回一个字典，其中包含一个人的姓名"""
	person={'first':first_name,'last':last_name}
	#返回了字典
	return person
person1=person_dic("xie","ru")
print(person1)
