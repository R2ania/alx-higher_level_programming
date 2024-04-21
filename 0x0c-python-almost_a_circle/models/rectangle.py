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
		self.validate_int("width", value, False)
		self.__width = value

	@property
	def height(self):
		'''height of the rectangle'''
		return self.__height

	@height.setter
	def height(self, value):
		self.validate_int("height", value, False)
		self.__height = value

	@property
	def x(self):
		''' x of rectangle'''
		return self.__x

	@x.setter
	def x(self, value):
		self.validat_int("x", value)
		self.__x = value

	@property
	def y(self):
		'''y of rectangle'''
		return self.__y

	@y.setter
	def y(self, value):
		self.validate_int("y", value)
		self.__y = value

	def Validat_int(self, name, value,  eg=True):
		''' function that validate value'''
		if type(value) != int:
			raise TypeError("{} must be an integer".format(name))
		if eg and value < 0:
			raise ValueError("{} must be > 0".format(name))
		elif not eg and value <= 0:
			raise ValueError("{} must be > 0".format(name))


	def area(self):
		'''computes the area of rectangle'''
		return self.width *  self.height

