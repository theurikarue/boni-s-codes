#Python program that takes a string as input and outputs the number of vowels in the string
def vowel_count(str):
    count=0
    vowel=set("aeiouAEIOU")
    for alphabet in str:
        if alphabet in vowel :
            count=count+1
print("n of vowels in string :",count)

str="TheuriKarue"
vowel_count(str)

    
