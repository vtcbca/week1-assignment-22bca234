def pali():
    a=int(input("Enter the number > "))
    if isinstance(a,int):
        a=str(a)
        if a==a[::-1]:
            print(f"The number {a} is a pallindrome number")
        else:
            print(f"The number {a} is not a pallindrome number")
    else:
        print(f"The number {a} is not integer")
pali()
