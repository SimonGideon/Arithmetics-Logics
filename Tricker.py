for i in range(10):
	print('*'*(i+1))
# Write a program that outputs 100 lines, numbered 1 to 100, each with your name on it.
for i in range(10):
	print((i+1), ". ----> Your Name.")
# Write a program that uses a for loop to print the numbers 8, 11, 14, 17, 20, . . . , 83, 86, 89
for i in range(7, 93):
	print(i-3)
#Write a program that asks the user for their name and how many times to print it. The program should print out the user’s name the specified number of times
name = str(input("Enter Your Name: "))
no = int(input("Enter the number of times: "))
for i in range(no):
	print(name)
