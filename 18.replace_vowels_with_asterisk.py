# Function to Replace each vowel in the string with a specified astrisk


def replaceVowelsWithK(test_str, K):

	vowels = 'AEIOUaeiou'

	for ele in vowels:

		test_str = test_str.replace(ele, K)

	return test_str


K = "*"
input_str = "Bonface is a beginner in programming but will become pro soon"

print("Given String:", input_str)
print("Given Specified Character:", K)

print("After replacing vowels with the specified character:",
	replaceVowelsWithK(input_str, K))
