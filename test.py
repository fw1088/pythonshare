#/usr/bin/env python
#-*-coding:utf-8 -*-

'''
python 简单介绍
python 是动态语言和js类似，单不同于oc，java这样的静态语言
python依赖于自身的解释器执行，有点类似于java的jvm
同时python也是弱类型的语言，没有严格的类型限制
下面时大体介绍，可以在命令行下进行实践
'''

class Guoke:
	"""
	a test class for dynamic language
	"""
	def __init__(self):
		self.name = "meituan"
		self.age = 6
	def test(self):
		self.school = "Beijing"

if __name__ == '__main__':
	#class dynamic
	test = Guoke()
	test.hello = "Hello Dynamic"
	print test.name
	print test.age
	print test.hello
	test.test()
	print test.school
	#weak type
	ptr = 100
	print ptr
	ptr = "meituan"
	print ptr
	array = []
	array.append("mei")
	array.append("tuan")
	print array
	
	ptr = Guoke()
	print ptr.name
