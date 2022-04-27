# coding:utf-8
for value in range(1,21):
	print(value)
	
millnumbers=list(range(1,1000001))
#for value in millnumbers:
#	print(value)

print(min(millnumbers))
print(max(millnumbers))
print(sum(millnumbers))

for value in range(1,20,2):
	print(value)
	
numbers=[]
for value in range(1,10):
	value=value*3
	numbers.append(value)
print(numbers)

for value in range(1,10):
	value=value**3
	numbers.append(value)
print(numbers)

number=[value**3 for value in range(1,10)]
print(number)





