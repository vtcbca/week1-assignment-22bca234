#2.Write a python script to enter any number and print the sum of its digit.
def digsum():
    n=int(input('Enter a number whose sum you want to print : '))
    sum=0
    while (n>0):
        a=n%10
        sum=sum+a
        n=n//10
    print(sum)
digsum()
