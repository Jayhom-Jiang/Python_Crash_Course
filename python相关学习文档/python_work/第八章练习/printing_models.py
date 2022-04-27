# coding: utf-8
# 在函数中修改列表，能大大提高扩展维护效率
# 对于函数中的列表是
def print_models(unprint_designs,completed_models):
	"""打印未完成的设计品"""
	while unprint_designs:
		current_designs=unprint_designs.pop()
		print("unprint_designs: "+ current_designs)
		completed_models.append(current_designs)

def show_completed_models(completed_models):
	"""打印做好的模型"""
	print("Completed models : ")
	for com_mod in completed_models:
		print(com_mod)

unprint_designs=['apple','peer','banana']
completed_models=[]

print_models(unprint_designs,completed_models)
show_completed_models(completed_models)
# 列表已经发生了改变
print(unprint_designs)
