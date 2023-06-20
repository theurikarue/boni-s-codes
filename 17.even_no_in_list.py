# Python program to print Even Numbers in a List
list1 = [10, 21, 4, 45, 66, 93, 69, 20]
for num in list1:

	if num % 2 == 0:
		print(num, end=" \n")

#using list comprehension
list1 = [10, 21, 4, 45, 66, 93, 69, 20]
even_numbers = [num for num in list1 if num % 2 == 0]
print(even_numbers)

