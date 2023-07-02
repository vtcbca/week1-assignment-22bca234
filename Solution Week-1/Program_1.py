#P1:-Write a python script to enter any number and check its prime or not.
def prime():
    a=int(input("Enter any number :"))
    for i in range(2,a):
        if a%i==0:	
            print("The number is not prime !")
            break
    else:
        print("The number is prime !")
prime()
