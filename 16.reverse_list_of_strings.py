# Python3 code to demonstrate Reverse All Strings in String List using list comprehension

# initializing list
test_list = ["Jehovah", "is", "my", "Lord", "and","Saviour"]

# printing original list
print ("The original list is : " + str(test_list))
# Reverse All Strings in String List using list comprehension
rev = [i[::-1] for i in test_list]
# printing result
print ("The reversed string list is : " + str(rev))
