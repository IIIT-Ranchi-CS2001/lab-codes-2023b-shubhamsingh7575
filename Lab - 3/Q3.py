n = int(input("Enter Number"))
a = 0
b = 1

# print("0 1 ", end="")

# temp = l + r

# n-=2

while n!=0:
    print(a,end =" ")
    temp = a+b
    a=b
    b=temp
    n=n-1