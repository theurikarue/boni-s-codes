test_list = ['girl', 'boy', 'best', 'for', 'Jesus']

# create a new list of string lengths using a list comprehension
lengths = [len(s) for s in test_list]

# find the index of the longest string in the original list
longest_index = lengths.index(max(lengths))

# use the index to get the longest string from the original list
longest_string = test_list[longest_index]

# print the longest string
print("Longest string is : " + longest_string)
