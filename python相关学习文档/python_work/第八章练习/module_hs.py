# coding: utf-8
# 第一种方法采用import python文件  然后用 python文件名.函数名(有实参或者无实参)
#import make_pizza
#make_pizza.maked_pizza('beef')
#make_pizza.maked_pizza('beef','extra cheese','mushrooms')

# 使用as给模块指定别名
import make_pizza as p
p.maked_pizza('beef')
p.maked_pizza('beef','extra cheese','mushrooms')

# 第二种方法，导入特定的函数 用：from python文件 import 函数名，函数名，函数名 ,然后用 函数名(有实参或者无实参)
from make_pizza import maked_pizza
maked_pizza('beef')
maked_pizza('beef','extra cheese','mushrooms')

# 使用as给导入函数指定别名
from make_pizza import maked_pizza as mp
mp('beef')
mp('beef','extra cheese','mushrooms')


