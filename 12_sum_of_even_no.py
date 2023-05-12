#Python program that takes a list of integers as input and outputs the sum of the even integers in the list.
sum=0
for i in range(100):
    if i%2==0:
        sum=sum+1

print("sum of even integers is: ",sum)