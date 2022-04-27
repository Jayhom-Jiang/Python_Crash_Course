# coding: utf-8
books={}
flag=True
while flag:
	auth=input("Please tell me your favoriate author’s name :")
	print(auth)
	book=input("The author writen books's name :")
	print(book)
# 因为input()函数就直接可以将变量赋值为字符串，所以下面的添加字典中的键-值对就不用再用双引号来表示字符串 比如 books[’auth‘]=’book‘
	books[auth]=book
	goon=input("If you want to end the talking , you can input 'no' ")
	if(goon=='no'):
		break;

for k,y in books.items():
	print("key: "+k+"  values: "+y)

# 在此之前，所有写的pytho文件都没有办法在字符串中出现，否则会报错，但是调整了utf—8之后的新文件就可以出现
