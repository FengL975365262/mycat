#coding:utf8

class Page():
	
	pageSize = property()
	pageNum = property()
	pageCount = property()
	pageResults = property()
	
	def __init__(self):
		self.__pageSize = 10
		self.__pageNum = 1
		self.__pageCount = 0
		self.__pageResults = []
	
	def myprint(self):
		print('hello world')
	
	@pageSize.getter
	def pageSize(self):
		return self.__pageSize
		
	@pageSize.setter
	def pageSize(self,value):
		self.__pageSize = value
	
	@pageNum.getter
	def pageNum(self):
		return self.__pageNum
		
	@pageNum.setter
	def pageNum(self,value):
		self.__pageNum = value
		
	@pageCount.getter
	def pageCount(self):
		return self.__pageCount
		
	@pageCount.setter
	def pageCount(self,value):
		self.__pageCount = value
		
	@pageResults.getter
	def pageResults(self):
		return self.__pageResults
		
	@pageResults.setter
	def pageResults(self,value):
		self.__pageResults = value