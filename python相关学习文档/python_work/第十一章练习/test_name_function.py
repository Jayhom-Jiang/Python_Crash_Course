# coding: utf-8
# 导入unittest模块
import unittest
from name_function import get_formatted_name

# 创建一个测试类前提是必须继承unnitest.TestCase类
class NamesTestCase(unittest.TestCase):
	"""测试name_function.py"""

	#在运行此py文件时只有test开头的方法才会自动运行
	def test_first_last_name(self):
		"""能够正确处理像 Job BOb这样的姓名吗？"""
		# 调用引入name_function.py的函数get_formatted_name
		formatted_name=get_formatted_name('job','bob')
		# 断言方法：再调用unittest的方法assertEqual进行测试布尔类型判断
		self.assertEqual(formatted_name, 'Job Bob' )

# 运行unittest.main()是让python运行这个文件中的测试
unittest.main()
