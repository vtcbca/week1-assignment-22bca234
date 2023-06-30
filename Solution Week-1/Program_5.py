#Write a python script to enter any string and count vowel.
def count_vowels():
    c=input("Enter any string : ")
    count=0
    list=['a','e','i','o','u','A','E','I','O','U']
    for i in c:
        if(i in list):
            count+=1
    print("Tne number of vowels in entered string is :",count)
count_vowels()
