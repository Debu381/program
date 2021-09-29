def fact(n):
    if n<=1:
        return 1
    else:
        n=n*fact(n-1)
        return n
n=int(input("enter the number:")) 
print("factorial Of ",n,"is",fact(n))        