# Function to count the number of vowels in a word
def count_vowels(word):
	# A string of all vowels
	vowels = "aeiouAEIOU"
	# Return the count of vowels in the word
	return sum(c in vowels for c in word)


def sort_strings(strings):
	
	return sorted(strings, key=count_vowels)


if __name__ == "__main__":
	# Input list of strings
	strings = ["lmno", "jkl", "aeiou", "collins"]
	sorted_strings = sort_strings(strings)
	
	print(sorted_strings)