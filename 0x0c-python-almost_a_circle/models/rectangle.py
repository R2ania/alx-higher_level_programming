#!/usr/bin/python3
''' Make A Rectangle'''
from models/base import Base



class Rectangle(Base):
	''' class Rectangle that inherts from Base'''

	def __init__(self, width, height, x, y, id=None):
		''' constructor'''
		super().__init__(id)
		self.width = width
		self.height = height
		self.x = x
		self.y = y

	@property
	def width(self):
		'''width of the rectangle'''
		return self.__width

	@width.setter
	def width(self, value):
		self.__width = value

	@property
	def height(self):
		'''height of the rectangle'''
		return self.__height

	@height.setter
	def height(self, value):
	self.__height = value

	@property
	def x(self):
		''' x of rectangle'''
		return self.__x

	@x.setter
	def x(self, value):
		self.__x = value

	@property
	def y(self):
		'''y of rectangle'''
		return self.__y

	@y.setter
	def y(self, value):
		self.__y = value

