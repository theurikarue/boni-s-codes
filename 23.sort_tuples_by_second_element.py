# Python program to sort a list of tuples by the second Item

def Sort_Tuple(tup):

	# getting length of list of tuples
	lst = len(tup)
	for i in range(0, lst):

		for j in range(0, lst-i-1):
			if (tup[j][1] > tup[j + 1][1]):
				temp = tup[j]
				tup[j] = tup[j + 1]
				tup[j + 1] = temp
	return tup



tup = [('again', 24), ('is', 10), ('christian', 28),
	('Bonface', 5), ('born', 20), ('a', 15)]

print(Sort_Tuple(tup))
