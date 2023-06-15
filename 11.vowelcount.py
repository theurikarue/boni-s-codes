  
#Python program that takes a string as input and outputs the number of vowels in the string
def vowel_count(str):
    count = 0
    vowel = set("aeiouAEIOU")
    for alphabet in str:
        if alphabet in vowel:
            count = count + 1
    print("Number of vowels in the string:", count)

str = input("Enter string")
vowel_count(str)

