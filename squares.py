import math
def square(x):
	return x*x
print(square(5))
# The existing function can be used to define another one
def sum_of_squares(x, y):
	return square(x) + square(y)
print(sum_of_squares(2, 3))
# One can't change a global varriable inside a function; Local Varriable- Varriables inside a function
x = 0
y = 0
def incr(x):
	y = x + 1
	return y
incr(5)
print(x, y)
# Area of circle
pi = math.pi
def area(r):
	return pi * r**2
r = eval(input("Radius: "))
print(area(r))
# To modify a global varriable you must declare a varriable global.
numcalls = 0
def square(x):
	global numcalls
	numcalls = numcalls + 1
	return x * x
x = 
def f():
	x = 2
	return x
print(x)
print(f())
# Global varriable can be used and out of the function.

