count=0 # division counter
n=int(input("enter the number :"))

for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2: #2 if prime 
    print(n,"is a prime number") 
else:
    print(n,"is a not prime number")          