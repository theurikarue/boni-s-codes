#Write a Python program that takes a list of integers as input and outputs a new list with the integers sorted in descending order
n=int(input("enter no of integers in list:  "))
listl=[]
for i in range(n):
    integer=int(input("Enter the elements in list"))
    listl.append(integer)
    print("Elements in list are: ",listl)
    listl.sort(reverse=True)
    print(listl)


