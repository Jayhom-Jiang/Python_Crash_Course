# coding: utf-8

def word_count(filename):
	"""计算一个文件大概有多少单词"""
		# 就是open()函数打开文件这里打开异常所以要放在try模块里面
	try:
		with open(filename) as file_object:
			content=file_object.read()
	except FileNotFoundError:
		#print("The file "+filename+" dose not exit!")
		#python中的 pass 语句可以不出现traceback然后直接跳过异常继续执行
		pass
	else:
		# 计算文件中大概有多少个单词
		# split()函数将文件读取的内容按照空格分开然后变成列表
		words=content.split()
		num_words=len(words)
		print("The file words number is : "+str(num_words))

filenames=['alice.txt','little_women.txt','siddhartha.txt','moby_dict.txt']
for filename in filenames:
	word_count(filename)
