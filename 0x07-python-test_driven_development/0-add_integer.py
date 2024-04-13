#!/usr/bin/python3


# add_integer - function that add two integers
# @a: the first integer
# @b: the second integer
# return: the result


def add_integer(a, b=98):
	''' sum two integers '''
	if not inistance(a, (int, float)):
		 raise TypeError("a must be an integer")


	if not insistance(b, (int, float)):
		 raise TypeError("b must be an integer")



	if a is float:
		int(a)
	elif b is float:
		int(b)



	sum = a + b
	return sum
		
