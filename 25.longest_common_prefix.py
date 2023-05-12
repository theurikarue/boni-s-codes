# Python 3 program to find longest common prefix of given array of words.
def longestCommonPrefix( a):
	
	size = len(a)

	# if size is 0, return empty string
	if (size == 0):
		return ""

	if (size == 1):
		return a[0]

	
	a.sort()
	
	
	end = min(len(a[0]), len(a[size - 1]))

	# find the common prefix between the first and last string
	i = 0
	while (i < end and
		a[0][i] == a[size - 1][i]):
		i += 1

	pre = a[0][0: i]
	return pre

# Driver Code
if __name__ == "__main__":

	input = ["disadvantage", "discontinue",
					"disco", "display"]
	print("The longest Common Prefix is :" ,
				longestCommonPrefix(input))


