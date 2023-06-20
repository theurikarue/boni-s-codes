# Python3 code to demonstrate Reverse All Strings in String List using list comprehension

# initializing list
test_list = ["Jehovah", "is", "my", "Lord", "and","Saviour"]

# printing original list
print ("The original list is : " + str(test_list))
# Reverse All Strings in String List using list comprehension
rev = [i[::-1] for i in test_list]
# printing result
print ("The reversed string list is : " + str(rev))


#alternatively
def reverse_strings(string_list):
    reversed_list = [string[::-1] for string in string_list]
    return reversed_list

# Test the function
string_list = ["Hello", "World", "Python"]
reversed_list = reverse_strings(string_list)
print(reversed_list)
