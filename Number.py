from math import *
from random import randint
# Write a program that generates and prints 50 random integers, each between 3 and 6
for i in range(50):
	x = randint(3, 6)
	print(x)
# Write a program that generates a random number, x, between 1 and 50, a random number y
# between 2 and 5, and computes x y
x = randint(1, 50)
y = randint(2, 5)
print(x**y)
# #Write a program that generates a random number between 1 and 10 and prints your name
# that many times
n = randint(1, 10)
for i in range(n):
	print("Your Name")
dec =float(randint(1, 10))
print(round(dec, 3))