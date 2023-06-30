#Write a python script to enter any number, if it is integer number, then check its armstrong or not. Print appropriate message if it is not armstrong.
def arm():
    b=input("Enter any  number >  ")
    sum=0
    for i in range(len(b)):
        sum+=int(b[i])**3

    if sum==int(b):
        print(f"The number {b} is a armstrong number")
    else:
        print(f"The number {b} is not a armstrong number")
arm()
