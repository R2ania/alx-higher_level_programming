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


	def display(self):
		'''prints the rectangle'''
		r = '\n' * self.y + \
			(' ' * self.x + '#' * self.width + '\n') * self.height
		print(r, end=' '


	def __str__(self):
		'''Returning string info of rectangle'''
		return ' [{}] ({}) {} - {}/{}'.\ 
			format(type(self).__name__, self.id, self.x, self.y,\
			self.width, self.height)


	def __update(self, id=None, width=None, height=None, x=None, y=None)
		''' update instance attributes'''
		if id is not None:
			self.id = id
		if width is not None:
			self.width = width
		if height is not None:
			self.height = height
		if x is not None:
			self.x = x
		if y is not None:
			self.y = y


	def Update(self, *args, **kwargs):
		'''update instance attributes via args'''
		# print(args, kwargs)
		if args:
			self.__update(*args)
		elif kwargs:
			self.__update(**kwargs)

