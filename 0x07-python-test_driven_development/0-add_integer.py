#!/usr/bin/python3




def add_integer(a, b=98):
	''' sum two integers '''
	if not inistance(a, (int, float)):
		 raise TypeError("a must be an integer")


	if not insistance(b, (int, float)):
		 raise TypeError("b must be an integer")


	return int(a) + int(b)



if __name__ == "__main__":
	import doctest
	doctest.testfile("tests/0-add_integer.txt")











		
