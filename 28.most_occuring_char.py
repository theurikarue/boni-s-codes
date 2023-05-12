# python code to find most occurring character in a string and its count
string1="jokesinsidejokes"
list1=[]
list2=[]
for i in string1:
	if i not in list1:
		list1.append(i)
	import operator
	list2.append(operator.countOf(string1,i))

occ=max(list2)
ele=list1[list2.index(occ)]
print(ele,occ)
