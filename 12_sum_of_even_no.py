#Python program that takes a list of integers as input and outputs the sum of the even integers 
num_list = []
even_sum = 0
for i in range(5):
    num = int(input("Enter an integer: "))
    num_list.append(num)
    if num % 2 == 0:
        even_sum += num
print("Sum of even integers:", even_sum)
