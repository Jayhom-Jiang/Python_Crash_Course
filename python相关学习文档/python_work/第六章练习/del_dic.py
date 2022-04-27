# coding:utf-8
# 删除键-值对
fish={'variety':'goldfish','color':'gold','length':'3cm'}
print(fish)
# 删除的键-值对永远消失，采用：del 字典['键名']
del fish['length']
print(fish)
