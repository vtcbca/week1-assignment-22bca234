#2.Write a python script to enter any number and print the sum of its digit.
def sum():
    n=int(input("Enter a number : "))
    s=0
    for i in range(n+1):
        s=s+i
    print(s)
sum()
