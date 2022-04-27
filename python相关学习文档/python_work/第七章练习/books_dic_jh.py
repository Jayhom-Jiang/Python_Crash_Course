# coding: utf-8
books={}
flag=True
while flag:
	auth=input("Please tell me your favoriate author¡®s name :")
	print(auth)
	book=input("The author writen books's name :")
	print(book)
	books['auth']='book'
for k,y in books.items():
	print("key:"+k+"values:"+y)
